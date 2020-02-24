## importing the required module and setting up the Flask-RESTful application
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

#creating list of users
users = [
    {
        "name": "Amy",
        "age": 42,
        "occupation": "Network Engineer"
    },
    {
        "name": "Ida",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "name": "Adam",
        "age": 22,
        "occupation": "Web Developer"
    }
]


## creating our API endpoints by defining a User resource class and it hulds
## four functions which correspond to four HTTP request method
class User(Resource):
    def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200
        
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200

## adding resource to the api and specifying its route      
api.add_resource(User, "/user/<string:name>")

app.run(debug=True)