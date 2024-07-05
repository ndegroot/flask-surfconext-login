"""Flask APP configuration."""
from os import environ, path
from dotenv import load_dotenv


# Specify a `.env` file containing key/value config values
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

SURFCONEXT_CLIENT_ID = environ.get('SURFCONEXT_CLIENT_ID')
SURFCONEXT_CLIENT_SECRET = environ.get('SURFCONEXT_CLIENT_SECRET')
