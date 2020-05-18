from os import abort

from flask import Flask, json
import requests
from BasePost import BasePost
from JsonablePost import JsonablePost
from Helper import Helper

app = Flask(__name__)

remote_api_url = 'https://jsonplaceholder.typicode.com/posts'
blog_posts = {}
helper = Helper()


@app.route("/posts")
def get_all_blog_posts():
    posts = []
    for post_id in blog_posts:
        posts.append(blog_posts[post_id].to_json())

    response = app.response_class(
        response=json.dumps(posts),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/posts/<int:post_id>")
def get_blog_post_by_id(post_id):
    if post_id not in blog_posts:
        abort(404)

    post_obj = blog_posts[post_id]

    json_response = post_obj.to_json()
    response = app.response_class(
        response=json.dumps(json_response),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/posts/user/<int:user_id>")
def get_blog_posts_by_user(user_id):
    blog_post_for_user = helper.filter_blog_post_by_user(user_id, blog_posts)
    response = app.response_class(
        response=json.dumps(blog_post_for_user),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/')
def hello_world():
    return 'Hello, World!'



# @app.route('/posts/<postId>/comments')
# def get_user_comment(postId):
#     id_tweet = requests.get('https://jsonplaceholder.typicode.com/posts/' + postId + '/comments')
#     posts = id_tweet.json()
#     response = app.response_class(
#         response=json.dumps(posts),
#         status=200,
#         mimetype='application/json'
#     )
#     return response


@app.before_first_request
def before_first_request_func():
    global blog_posts
    response = requests.get(remote_api_url)
    data = response.json()

    for post in data:
        jsonable_post = JsonablePost(post)
        blog_posts[jsonable_post.id] = jsonable_post


if __name__ == "__main__":
    app.run()
