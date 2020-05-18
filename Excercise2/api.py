from flask import Flask, json, request, abort
from Instrument import GetInstruments, GetUser, addNewInstrument, addNewUser


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/instruments')
def get_all_instruments():
    response = app.response_class(
        response=json.dumps(GetInstruments()),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/user')
def get_user():
    response = app.response_class(
        response=json.dumps(GetUser()),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/add/instruments/<type>', methods=["GET", "POST"])
def add_new_instrument(type):
    addNewInstrument({"type": type})
    response = app.response_class(
        response=json.dumps({"type": type}),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/add/user', methods=["GET", "POST"])
def add_new_user():
    content = request.json
    new_user_to_add = {
        "firstName": content["firstName"],
        "lastName": content["lastName"]
    }
    addNewUser(new_user_to_add)
    response = app.response_class(
        response=json.dumps(new_user_to_add),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run()
