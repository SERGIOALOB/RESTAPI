import logging

import requests
from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_restful import Api as _Api, Resource, HTTPException
from flask_sqlalchemy import SQLAlchemy
from requests.exceptions import HTTPError

app = Flask(__name__)

class Api(_Api):
    def error_router(self, original_handler, e):
        # Override original error_router to only handle HTTPExceptions.
        if self._has_fr_route() and isinstance(e, HTTPException):
            try:
                # Use Flask-RESTful's error handling method
                return self.handle_error(e) 
            except Exception:
                # Fall through to original handler (i.e. Flask)
                pass
        return original_handler(e)

api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@flask_mysql:3306/db"
db = SQLAlchemy(app)
ma = Marshmallow(app)

if db is None:
    db.create_all()
    db.session.commit()


class Post(db.Model):
    __tablename__ = "Post"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    github_name = db.Column(db.String(100))
    github_following = db.Column(db.Integer)


@app.before_first_request
def create_tables():
    db.create_all()


class PostSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "name",
            "surname",
            "lastname",
            "github_name",
            "github_following",
        )
        model = Post


post_schema = PostSchema()
posts_schema = PostSchema(many=True)


class PostsResource(Resource):
    def get(self):
        return posts_schema.dump(Post.query.all())

    def post(self):
        data = request.json
        post = Post(
            name=data["name"],
            surname=data["surname"],
            lastname=data["lastname"],
            github_name=data["github_name"],
            github_following=get_following(data["github_name"]),
        )
        db.session.add(post)
        db.session.commit()
        return post_schema.dump(post)


class PostResource(Resource):
    def get(self, pk):
        return post_schema.dump(Post.query.get_or_404(pk))

    def patch(self, pk):
        data = request.json
        post = Post.query.get_or_404(pk)

        if "name" in data:
            post.name = data["name"]

        if "surname" in data:
            post.surname = data["surname"]

        if "lastname" in data:
            post.lastname = data["lastname"]

        if "github_name" in data:
            post.github_name = data["github_name"]

        if "github_following" in data:
            post.github_following = get_following(post.github_name)

        db.session.commit()
        return post_schema.dump(post)

    def delete(self, pk):
        post = Post.query.get_or_404(pk)
        db.session.delete(post)
        db.session.commit()
        return "", 204

class APIException(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv
    
@app.errorhandler(APIException)
def handle_my_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response   


def get_following(github_name):
    try:
        url = f"https://api.github.com/users/{github_name}/following"
        response = requests.get(url=url)
        response.raise_for_status()
        print(response)
        following = [following_item['login'] for following_item in response.json() if 'login' in following_item]
        return len(following)
    except(HTTPError, KeyError, TypeError) as e:
        logging.warning(f'User not found {response.json()}')
        raise APIException('Github user not found', status_code=400)


api.add_resource(PostResource, "/post/<int:pk>")
api.add_resource(PostsResource, "/posts")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
