# Surfconext login demo with Flask

You can learn how the Flask OAuth 2.0 client works with OpenID with this demo.

## Install

Install the required dependencies:
Use `Poetry install` with supplied `pyproject.toml` or 

    $ pip install -U Flask Authlib requests python-dotenv

## Config

Create your Surf Conext OpenID Client using the Dashboard 
see <https://wiki.surfnet.nl/display/surfconextdev/Connect+in+5+Steps> for info, 
make sure to add `http://127.0.0.1:5000/auth` into the list of Authorized redirect URIs.

Fill the given client ID and secret into an new .env file which is read into `config.py`.

Put the client_id and the secret you obtained inside this file

``` env
SURFCONEXT_CLIENT_ID = '[the client id]'
SURFCONEXT_CLIENT_SECRET = '[the client secret]'
```

## Run

Start server with:

    $ export FLASK_APP=app.py
    $ flask run

Then visit:

    http://127.0.0.1:5000/

You should see a page with a login link. 
Using that you should receive a dict with keys and values:

```
{"acr": "urn:federation:authentication:windows", 
"aud": "...", 
"auth_time": 1720195698, 
"exp": 1720199298, 
"iat": 1720195698, 
"iss": "https://connect.test.surfconext.nl", 
"jti": "...", 
"nbf": 1720195698, 
"nonce": "...", 
"scope": "openid", 
"sub": "..."}
```


