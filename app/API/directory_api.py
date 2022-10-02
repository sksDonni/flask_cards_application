import json
from app import db, api
from flask import jsonify, make_response, request
from flask_restful import Resource
from app.models import Directory, DirectorySchema, User
from flask_security import auth_required, current_user

class DirectoryAPI(Resource):
    @auth_required("token")
    def get(self):
      records = Directory.query.filter_by(user_id=current_user.user_id)
      directory_schema = DirectorySchema(many=True)
      print(records)
      if records:
        return jsonify(directory_schema.dump(records))
      else:
        error_dict = {"message":"dirs were not found in the database"}
        response = make_response(jsonify(error_dict), 401)
        response.headers["Content-Type"] = "application/json"
        return response

    @auth_required('token')
    def post(self):
      directory_schema = DirectorySchema()
      print(request.json)
      if request.json:
        body = str(request.json)
        print(type(request.json))
        body = body.replace("\'", "\"")
        body = json.loads(body)
        print(body)

      dir_name = body['dir_name']
      print(current_user.user_id)
      user_id = current_user.user_id

      new_department = Directory(dir_name=dir_name, user_id=user_id)
      print(new_department)
      db.session.add(new_department)
      a = jsonify(directory_schema.dump(new_department))
      db.session.commit()
      return a


class IndividualDirectoryAPI(Resource):
    @auth_required('token')
    def get(self, id):
      directory_schema = DirectorySchema()
      record = Directory.query.get(id)
      print(record)
      if record == None:
        error_dict = {"message":"department id not found in the database"}
        response = make_response(jsonify(error_dict), 401)
        response.headers["Content-Type"] = "application/json"
        return response
      else:
        if record.user_id == current_user.user_id:
          return jsonify(directory_schema.dump(record))
        else:
          error_dict = {"message":"You are not authorized"}
          response = make_response(jsonify(error_dict), 401)
          response.headers["Content-Type"] = "application/json"
          return response
    
    @auth_required('token')
    def put(self, id):
      directory_schema = DirectorySchema()
      record = Directory.query.get(id)
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
          dir_name = body['dir_name']
          user_id = current_user.user_id
          record.dir_name = dir_name
          record.user_id = current_user.user_id
          db.session.commit()
          return jsonify(directory_schema.dump(record))
        else:
          error_dict = {"message":"You are not authorized"}
          response = make_response(jsonify(error_dict), 401)
          response.headers["Content-Type"] = "application/json"
          return response
    
    @auth_required('token')
    def delete(self, id):
      directory_schema = DirectorySchema()
      record = Directory.query.get(id)
      if record == None:
        error_dict = {"message":"Department id not found in the database"}
        response = make_response(jsonify(error_dict), 401)
        response.headers["Content-Type"] = "application/json"
        return response
      else:
        if record.user_id == current_user.user_id:
          db.session.delete(record)
          db.session.commit()
          return jsonify(directory_schema.dump(record))
        else:
          error_dict = {"message":"You are not authorized"}
          response = make_response(jsonify(error_dict), 401)
          response.headers["Content-Type"] = "application/json"
          return response


api.add_resource(DirectoryAPI, '/api/directory')
api.add_resource(IndividualDirectoryAPI, '/api/directory/<int:id>')
