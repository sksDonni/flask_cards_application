import json
from warnings import catch_warnings

from flask_security import auth_required
from app import db, api
from flask import jsonify, make_response, request
from flask_restful import Resource
from app.models import Deck, DeckSchema
from flask_security import auth_required, current_user

class DeckAPI(Resource):
    @auth_required('token')
    def get(self):
      records = Deck.query.filter_by(user_id=current_user.user_id)
      print(records)
      if records:
        deck_schame = DeckSchema(many=True)
        return jsonify(deck_schame.dump(records))
      else:
        error_dict = {"message":"dirs were not found in the database"}
        response = make_response(jsonify(error_dict), 401)
        response.headers["Content-Type"] = "application/json"
        return response

    @auth_required('token')
    def post(self):
      deck_schema = DeckSchema()
      print(request.json)
      if request.json:
        body = str(request.json)
        print(type(request.json))
        body = body.replace("\'", "\"")
        body = json.loads(body)
        print(body)

      deck_name = body['deck_name']
      dir_id = body['dir_id']
      user_id = current_user.user_id

      new_deck = Deck(dir_id=dir_id, user_id=user_id, deck_name=deck_name)
      print(new_deck)
      db.session.add(new_deck)
      db.session.commit()
      return jsonify(deck_schema.dump(Deck.query.all()[-1]))


class IndividualDeckAPI(Resource):
    @auth_required('token')
    def get(self, id):
      deck_schema = DeckSchema()
      record = Deck.query.get(id)
      print(record)
      if record == None:
        error_dict = {"message":"department id not found in the database"}
        response = make_response(jsonify(error_dict), 401)
        response.headers["Content-Type"] = "application/json"
        return response
      else:
        if record.user_id == current_user.user_id:
          return jsonify(deck_schema.dump(record))
        else:
          error_dict = {"message":"You are not authorized"}
          response = make_response(jsonify(error_dict), 401)
          response.headers["Content-Type"] = "application/json"
          return response
    
    @auth_required('token')
    def put(self, id):
      deck_schema = DeckSchema()
      record = Deck.query.get(id)
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
          deck_name = body['deck_name']
          dir_id = body['dir_id']
          user_id = current_user.user_id
          dir_level = body['dir_level']

          record.deck_name = deck_name
          record.dir_id = dir_id
          record.user_id = user_id
          record.dir_level = dir_level

          db.session.commit()
          return jsonify(deck_schema.dump(record))
        else:
          error_dict = {"message":"You are not authorized"}
          response = make_response(jsonify(error_dict), 401)
          response.headers["Content-Type"] = "application/json"
          return response
    
    @auth_required('token')
    def delete(self, id):
      deck_schema = DeckSchema()
      record = Deck.query.get(id)
      if record == None:
        error_dict = {"message":"Department id not found in the database"}
        response = make_response(jsonify(error_dict), 401)
        response.headers["Content-Type"] = "application/json"
        return response
      else:
        if record.user_id == current_user.user_id:
          db.session.delete(record)
          db.session.commit()
          return jsonify(deck_schema.dump(record))
        else:
          error_dict = {"message":"You are not authorized"}
          response = make_response(jsonify(error_dict), 401)
          response.headers["Content-Type"] = "application/json"
          return response


api.add_resource(DeckAPI, '/api/deck')
api.add_resource(IndividualDeckAPI, '/api/deck/<int:id>')
