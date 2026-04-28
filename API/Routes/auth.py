from flask import request
from flask_restful import Resource
from Databse.models import UserModel
from Databse.Db import db
import bcrypt


class Register(Resource):
    def post(self):
        data = request.get_json()

        if UserModel.query.filter_by(userName=data['userName']).first():
            return {"message": "User already exists"}, 400\
            
        if UserModel.query.filter_by(email=data['email']).first():
            return {"message": "Email already exists"}, 400

        hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        new_user = UserModel(
            userName=data['userName'],
              password=hashed_password.decode('utf-8')
            , email=data['email']
              )
        db.session.add(new_user)
        db.session.commit()

        return {"message": "User registered successfully"}, 200
    
class Login(Resource):
    def post(self):
        data = request.get_json()
        user = UserModel.query.filter_by(username=data['username']).first()

        if not user:
            return {"message": "User not found"}, 404

        if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
            return {"message": "Login successful"}, 200
        else:
            return {"message": "Invalid credentials"}, 400