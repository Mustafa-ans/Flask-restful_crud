import pymongo
from flask import Flask
from bson.objectid import ObjectId
import os
from flask_restful import Resource
from flask_restful import Api
from flask_restful import reqparse


app = Flask(__name__)
api = Api(app)

try:
    mongo_uri = os.environ["MONGO_URI"]
    mongo = pymongo.MongoClient(mongo_uri, serverSelectionTimeoutMS=1000)
except:
    print("Error - connection error to db")

try:
    mongo = pymongo.MongoClient(host="localhost", port=27017, serverSelectionTimeoutMS=1000)
    db = mongo.user_db
    mongo.server_info()  # exception trigger
except:
    print("Error - connection error to db")

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help='Name cannot be blank')
parser.add_argument('email', type=str, required=True, help='Email cannot be blank')
parser.add_argument('password', type=str, required=True, help='Password cannot be blank')


class User(Resource):
    def post(self):
        args = parser.parse_args()
        user = {"name": args['name'],
                "email": args['email'],
                "password": args['password']}
        dbResponse = db.users.insert_one(user)
        return {"message": "User created", "id": str(dbResponse.inserted_id)}, 200

    def get(self):
        data = list(db.users.find())
        for user in data:
            user["_id"] = str(user["_id"])
        return data, 200


class UserUpdate(Resource):
    def patch(self, id):
        args = parser.parse_args()
        dbResponse = db.users.update_one({"_id": ObjectId(id)},
                                         {"$set": {"name": args['name'],
                                                   "email": args['email'],
                                                   "password": args['password']}})
        if dbResponse.modified_count == 1:
            return {"message": "Details updated"}, 200
        else:
            return {"message": "Details entered were the same as before"}, 200

    def delete(self, id):
        dbResponse = db.users.delete_one({"_id": ObjectId(id)})
        if dbResponse.deleted_count == 1:
            return {"message": "User successfully deleted", "id": str(id)}, 200
        else:
            return {"message": "Invalid ID or user does not exist"}, 200


api.add_resource(User, '/users')
api.add_resource(UserUpdate, '/users/<string:id>')

if __name__ == "__main__":
    app.run()
