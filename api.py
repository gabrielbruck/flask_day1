from os import abort

from flask import Flask, json
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/posts/')
def get_posts():
    p = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = p.json()
    response = app.response_class(
        response=json.dumps(posts),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/posts/<todo_id>')
def post_id(todo_id):
    id_response = requests.get('https://jsonplaceholder.typicode.com/posts/' + todo_id)
    getID = id_response.json()
    response = app.response_class(
        response=json.dumps(getID),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/posts-by-userId/<userId>')
def get_user_id(userId):
    id_tweet = requests.get('https://jsonplaceholder.typicode.com/posts/?userId=' + userId)
    posts = id_tweet.json()
    response = app.response_class(
        response=json.dumps(posts),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/posts/<postId>/comments')
def get_user_comment(postId):
    id_tweet = requests.get('https://jsonplaceholder.typicode.com/posts/'+ postId +'/comments')
    posts = id_tweet.json()
    response = app.response_class(
        response=json.dumps(posts),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    app.run()
