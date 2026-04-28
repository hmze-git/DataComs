from Databse.Db import db
import uuid


class UserModel(db.Model):
    id=db.Column(db.String(50),primary_key=True,default=lambda: str(uuid.uuid4()))
    userName=db.Column(db.String(150),nullable=False,unique=True)
    email=db.Column(db.String(50),nullable=False,unique=True)
    password=db.Column(db.String(50),nullable=False)


    videos= db.relationship('Video',backref='uploader',lazy=True)
    def __repr__(self):
        return f"UserModel('{self.id}','{self.userName}','{self.email}','{self.passwprd}')"
    


class Video(db.Model):
    id=db.Column(db.String(50),primary_key=True,default=lambda: str(uuid.uuid4()))
    title=db.Column(db.String(150),nullable=False,unique=True)
    description=db.Column(db.Text,nullable=True)
    Fpath=db.Column(db.String(500),nullable=False)
    duration=db.Column(db.Integer,nullable=False)
    uploaded_by=db.Column(db.String(50),db.ForeignKey('user_model.id'),nullable=False)
    def __repr__(self):
        return f"videos('{self.id}','{self.title}','{self.description}','{self.Fpath}','{self.duration}')"