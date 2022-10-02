import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	DEBUG = True
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'WE WILL WIN!!!'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///'+os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = os.environ.get("SECRET_KEY", 'pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw')
	SECURITY_PASSWORD_SALT = os.environ.get("SECURITY_PASSWORD_SALT", '146585145368132386173505678016728509634')
	SQLALCHEMY_ENGINE_OPTIONS = {"pool_pre_ping": True}
	WTF_CSRF_ENABLED=False
	MAIL_SERVER =  'localhost'
	MAIL_PORT = 25
	MAIL_USE_TLS =  False
	MAIL_USE_SSL =  False
	MAIL_USERNAME =  None
	MAIL_PASSWORD =  None
	MAIL_DEFAULT_SENDER = None
	MAIL_MAX_EMAILS =  None
