from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)
ma = Marshmallow(app)


# @app.route('/posts', methods = ['POST', 'GET'])
# def home():
#	if request.method = 'POST':s
#		return {'data': 'Post request'}
#	if request.method = 'GET':
#		return {'data': 'Get request'}
#	return {'data': 'Hello world'}

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))


# def __repr__(self):
# return '<Post %s>' % self.name

class PostSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'surname', 'lastname')
        model = Post


post_schema = PostSchema()
posts_schema = PostSchema(many=True)


class PostsResource(Resource):
    def get(self):
        return posts_schema.dump(Post.query.all())

    def post(self):
        data = request.json
        post = Post(name=data['name'], surname=data['surname'], lastname=data['lastname'])
        db.session.add(post)
        db.session.commit()
        return post_schema.dump(post)


class PostResource(Resource):
    def get(self, pk):
        return post_schema.dump(Post.query.get_or_404(pk))

    def patch(self, pk):
        data = request.json
        post = Post.query.get_or_404(pk)

        if 'name' in data:
            post.name = data['name']

        if 'surname' in data:
            post.surname = data['surname']

        if 'lastname' in data:
            post.lastname = data['lastname']

        db.session.commit()
        return post_schema.dump(post)

    def delete(self, pk):
        post = Post.query.get_or_404(pk)
        db.session.delete(post)
        db.session.commit()
        return '', 204


api.add_resource(PostResource, '/post/<int:pk>')
api.add_resource(PostsResource, '/posts')

if __name__ == '__main__':
    app.run(debug=True)
