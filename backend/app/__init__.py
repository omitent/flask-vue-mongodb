import os
import json
import datetime
import logging
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from celery import Celery

class JSONEncoder(json.JSONEncoder):
    ''' extend json-encoder class'''

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)

app = Flask(__name__)
CORS(app)
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
app.config['JWT_SECRET_KEY'] = os.environ.get('SECRET')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
mongo = PyMongo(app)
flask_bcrypt = Bcrypt(app)
jwt = JWTManager(app)
app.json_encoder = JSONEncoder

gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_logger.handlers)
app.logger.setLevel(logging.DEBUG)

REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
app.config['CELERY_BROKER_URL'] = 'redis://{}:6379/0'.format(REDIS_HOST)
app.config['CELERY_RESULT_BACKEND'] = 'redis://{}:6379/0'.format(REDIS_HOST)
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

app.config['DEBUG'] = os.getenv('DEBUG') in [1, 'True', 'true']

from .admin import group, admin_auth
from .users import register, auth, refresh, user_endpoint
from .tasks.tasks import count_words
from .tasks.status import get_status
from .results import results, poll