from flask_sqlalchemy import *

db=SQLAlchemy()

class Profile(db.Model):
    
    __tablename__='user'
    id=db.Column(db.Integer,autoincrement=True,primary_key=True,unique=True)
    first_name=db.Column(db.String(25))
    last_name=db.Column(db.String(25))
    age=db.Column(db.Integer())
    phno=db.Column(db.Integer(),unique=True)

    def __init__(self,first_name,last_name,age,phno):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.phno=phno

    def json(self):
        return{'id':self.id,"first_name":self.first_name,"last_name":self.last_name,"age":self.age,"phno":self.phno}
