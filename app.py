from flask import Flask, jsonify
from flask_restful import Api, Resource, request
from models import db, Profile

app = Flask(__name__)

app.config['SQLALCHEMY_DATABSE_URI'] = 'sqlite:///teja.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


class ProfilesView(Resource):
    def get(self):
        user = Profile.query.all()
        return {"code":200,"message":"user data fetch successfully",'users': list(x.json() for x in user)}

    def post(self):
        data = request.get_json()

        new_user = Profile(data['first_name'], data['last_name'], data['age'], data['phno'])
        db.session.add(new_user)
        db.session.commit()
        return {"code":201,"message":"user data inserted successfully","user":(new_user.json())}



class ProfileView(Resource):
    def get(self, id):
        user = Profile.query.filter_by(id=id).first()

        if user:
            return {"code":200,"message":"user data fetch successfully",'user':user.json()}
        return {"code":404,'message': 'user not found'}

    def put(self, id):
        data = request.get_json()
        user = Profile.query.filter_by(id=id).first()
        if user:
            user.first_name=data["first_name"]
            user.last_name = data["last_name"]
            user.age=data["age"]
            user.phno = data["phno"]
        else:
            user = Profile(id=id, **data)
        db.session.add(user)
        db.session.commit()
        return {"code":200,"message":"user data update successfully",'user':user.json()}

    def delete(self, id):
        user = Profile.query.filter_by(id=id).first()

        if user:
            db.session.delete(user)
            db.session.commit()
            return {"code":204,"message": "user data delete successfully"}
        else:
            return {"code":404,"message": "user not found"}


api.add_resource(ProfilesView, '/user')
api.add_resource(ProfileView, '/user/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)
