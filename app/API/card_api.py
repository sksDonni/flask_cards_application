import json
import datetime
from sqlite3 import Date
from warnings import catch_warnings
from app import db, api
from flask import jsonify, make_response, request
from flask_restful import Resource
from app.models import Card, CardSchema
from flask_security import auth_required, current_user

class CardAPI(Resource):
    @auth_required('token')
    def get(self):
      records = Card.query.filter_by(user_id=current_user.user_id)
      print(records)
      if records:
        card_schema = CardSchema(many=True)
        return jsonify(card_schema.dump(records))
      else:
        error_dict = {"message":"dirs were not found in the database"}
        response = make_response(jsonify(error_dict), 401)
        response.headers["Content-Type"] = "application/json"
        return response

    @auth_required('token')
    def post(self):
      card_schema = CardSchema()
      print(request.json)
      if request.json:
        body = str(request.json)
        print(type(request.json))
        body = body.replace("\'", "\"")
        body = json.loads(body)
        print(body)

        category = 'simple'
        front = body['front']
        back = body['back']
        dir_id = body['dir_id']
        user_id = current_user.user_id
        deck_id = body['deck_id']

        new_card = Card(dir_id=dir_id, user_id=user_id, deck_id=deck_id
                              ,front=front, back=back, category=category)
        db.session.add(new_card)
        db.session.commit()
        latest_card = Card.query.all()[-1]
        print(latest_card)
        return jsonify(card_schema.dump(latest_card))
      else:
        error_dict = {"message":"dirs were not found in the database"}
        response = make_response(jsonify(error_dict), 401)
        response.headers["Content-Type"] = "application/json"
        return response


class IndividualCardAPI(Resource):
    @auth_required('token')
    def get(self, id):
      card_schema = CardSchema()
      record = Card.query.get(id)
      print(record)
      if record == None:
        error_dict = {"message":"department id not found in the database"}
        response = make_response(jsonify(error_dict), 401)
        response.headers["Content-Type"] = "application/json"
        return response
      else:
        if record.user_id == current_user.user_id:
          return jsonify(card_schema.dump(record))
        else:
          error_dict = {"message":"You are not authorized"}
          response = make_response(jsonify(error_dict), 401)
          response.headers["Content-Type"] = "application/json"
          return response
    
    @auth_required('token')
    def put(self, id):
      card_schema = CardSchema()
      record = Card.query.get(id)
      if request.json:
        body = str(request.json)
        print(type(request.json))
        body = body.replace("\'", "\"")
        body = json.loads(body)
        print(body)

      if record == None:
        error_dict = {"message":"Department id not found in the database"}
        response = make_response(jsonify(error_dict), 401)
        response.headers["Content-Type"] = "application/json"
        return response
      else:
        if record.user_id == current_user.user_id:
          category = 'simple'
          front = body['front']
          back = body['back']
          dir_id = body['dir_id']
          user_id = current_user.user_id
          deck_id = body['deck_id']
          card_level = body['card_level']

          record.front = front
          record.back = back
          record.dir_id = dir_id
          record.deck_id = deck_id
          record.user_id = user_id
          record.card_level = card_level

          db.session.commit()
          return jsonify(card_schema.dump(record))
        else:
          error_dict = {"message":"You are not authorized"}
          response = make_response(jsonify(error_dict), 401)
          response.headers["Content-Type"] = "application/json"
          return response
    
    @auth_required('token')
    def delete(self, id):
      card_schema = CardSchema()
      record = Card.query.get(id)
      if record == None:
        error_dict = {"message":"Department id not found in the database"}
        response = make_response(jsonify(error_dict), 401)
        response.headers["Content-Type"] = "application/json"
        return response
      else:
        if record.user_id == current_user.user_id:
          db.session.delete(record)
          db.session.commit()
          return jsonify(card_schema.dump(record))
        else:
          error_dict = {"message":"You are not authorized"}
          response = make_response(jsonify(error_dict), 401)
          response.headers["Content-Type"] = "application/json"
          return response


api.add_resource(CardAPI, '/api/card')
api.add_resource(IndividualCardAPI, '/api/card/<int:id>')
