from flask import Flask, url_for, session
from flask import render_template, redirect
from authlib.integrations.flask_client import OAuth


app = Flask(__name__)
app.secret_key = '!secret'
app.config.from_object('config')

CONF_URL = 'https://connect.test.surfconext.nl/.well-known/openid-configuration'
oauth = OAuth(app)
oauth.register(
    name='surfconext',  # becomes an attribute of oauth instance
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'openid'
    }
)


@app.route('/')
def homepage():
    user = session.get('user')
    return render_template('home.html', user=user)


@app.route('/login')
def login():
    redirect_uri = url_for('auth', _external=True)
    return oauth.surfconext.authorize_redirect(redirect_uri)


@app.route('/auth')
def auth():
    token = (oauth.surfconext.authorize_access_token())
    session['user'] = token['userinfo']
    return redirect('/')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')
