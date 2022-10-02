from email.policy import default
from tkinter.tix import DirSelectBox, Tree
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db, login, ma
from flask_security import UserMixin, RoleMixin

class RolesUsers(db.Model):
	__tablename__ = 'roles_users'
	__table_args__ = {'extend_existing': True}
	id = db.Column(db.Integer(), primary_key=True)
	user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.user_id'))
	role_id = db.Column('role_id', db.Integer, db.ForeignKey('role.id'))


class Card(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key = True)
	category = db.Column(db.String(100))
	front = db.Column(db.String(100), nullable=False)
	back = db.Column(db.String(100000), nullable=False)
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	dir_id = db.Column(db.Integer, db.ForeignKey('directory.dir_id'), nullable=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=True)
	deck_id = db.Column(db.Integer, db.ForeignKey('deck.deck_id'), nullable=True)
	card_level = db.Column(db.Integer, default=0)

class Deck(db.Model):
	deck_id = db.Column(db.Integer, primary_key=True)
	deck_name = db.Column(db.String(120))
	user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=True)
	dir_id = db.Column(db.Integer, db.ForeignKey('directory.dir_id'), nullable=True)
	dir_level = db.Column(db.Integer, default=0)
	deck_cards = db.relationship('Card', backref=db.backref('deck cards'), lazy='dynamic')

class Directory(db.Model):
	dir_id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=True) 
	dir_name  = db.Column(db.String(1000), nullable=False)
	dir_decks = db.relationship('Deck', backref=db.backref('dir deck'), lazy='dynamic')
	dir_cards = db.relationship('Card', backref=db.backref('dir_card'), lazy='dynamic')


class User(UserMixin, db.Model):
	user_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	firstname = db.Column(db.String(64))
	lastname = db.Column(db.String())
	email = db.Column(db.String(120), index=True, unique=True)
	password = db.Column(db.String(128))
	daily_limit = db.Column(db.Integer, default=100)
	active = db.Column(db.Boolean())
	dirs = db.relationship('Directory', backref=db.backref('user directories'), lazy='dynamic')
	decks = db.relationship('Deck', backref=db.backref('user decks'), lazy='dynamic')
	cards = db.relationship('Card', backref=db.backref('user cards'), lazy='dynamic')
	fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
	roles = db.relationship('Role', secondary='roles_users',
                         backref=db.backref('users', lazy='dynamic'))

	def __repr__(self):
		return 'User{}'.format(self.username)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class CardSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = Card()
		include_fk = True

class DeckSchema(ma.SQLAlchemyAutoSchema):
	deck_cards = ma.Nested(CardSchema, many=True)
	class Meta:
		model = Deck()
		include_fk = True

class DirectorySchema(ma.SQLAlchemyAutoSchema):
	dir_decks = ma.Nested(DeckSchema, many=True)
	dir_cards = ma.Nested(CardSchema, many=True)

	class Meta:
		model = Directory()
		include_fk = True

class UserSchema(ma.SQLAlchemyAutoSchema):
	dirs = ma.Nested(DirectorySchema, many=True)
	decks = ma.Nested(DeckSchema, many=True)
	cards = ma.Nested(CardSchema, many=True)

	class Meta:
		model = User()
		include_fk = True



