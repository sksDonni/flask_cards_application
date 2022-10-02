from crypt import methods
import json
from app import app, db, api, user_datastore, security
from flask import jsonify, make_response, request
from app.models import User, UserSchema, Role, RolesUsers
from flask_security.utils import hash_password


@app.route('/register', methods=['POST', 'GET'])
def register():
    print(request.__dict__)
    if request.method=="POST" and request.json:
        body = str(request.json)
        print(type(request.json))
        body = body.replace("\'", "\"")
        body = json.loads(body)
        print(body)

        user_datastore.create_user(
            email=body['email'],
            username=body['username'],
            firstname=body['firstname'],
            lastname=body['lastname'],
            password=hash_password(body['password'])
        )
        db.session.commit()
        user_schema = UserSchema()
        return jsonify(user_schema.dump(User.query.all()[-1]))
    else:
        print(request.json)
        return jsonify({"message":"error"}, 404)

@app.route('/loginuser', methods=['GET', 'POST'])
def new_login_user():
    if request.json:
        body = str(request.json)
        print(type(request.json))
        body = body.replace("\'", "\"")
        body = json.loads(body)
        print(body)

        record = User.query.filter_by(email=body['email']).first()
        print(record)

        return "yes"
    
    return "no"

    