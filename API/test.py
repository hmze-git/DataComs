from flask import Flask
from Databse.Db import db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Disbo%40rd@localhost/datacomms'

db.init_app(app)


@app.route('/')
def hello_world():
       return 'Hello, World!'

if __name__ == '__main__':
       from Databse.models import UserModel,Video
       with app.app_context():
              db.create_all()

       app.run(debug=True)
