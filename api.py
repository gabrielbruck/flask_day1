from flask import Flask, json
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/posts')
def post_id():
    p = request.get_json('https://jsonplaceholder.typicode.com/todos')
    posts = p.json()
    return post, 200


if __name__ == "__main__":
    app.run()
