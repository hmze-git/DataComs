from flask import Flask
from flask_restful import Resource, Api,reqparse,fields,marshal_with,abort
from Databse.Db import db
from Routes.auth import Register,Login
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Pass@db/datacomms'

db.init_app(app)
api=Api(app)

api.add_resource(Register,'/register')
api.add_resource(Login,'/login')

@app.route('/')
def hello_world():
       return 'Hello, World!'

if __name__ == '__main__':
       from Databse.models import UserModel,Video
       with app.app_context():
             # db.drop_all() # breks otherwise
              db.create_all()

       app.run(host='0.0.0.0', debug=True)
