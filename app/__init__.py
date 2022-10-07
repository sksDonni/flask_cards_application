from flask import Flask
from config import Config
from celery import Celery
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_cors import CORS
from flask_security import Security, SQLAlchemyUserDatastore, auth_required, hash_password
from flask_security.models import fsqla_v2 as fsqla

app = Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

app.config.from_object(Config)
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

db = SQLAlchemy(app)
fsqla.FsModels.set_db_info(db)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
ma = Marshmallow(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
api = Api(app)

from app import models
user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)
security = Security(app, user_datastore)
from app.API import directory_api, card_api, deck_api
from app.routes import register