from flask import Flask, json
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


@app.route('/users')
def get_users():
    response = app.response_class(
        response=json.dumps(GetUser()),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/add/instruments/<instrument_type>', methods=["POST"])
def add_new_instrument(instrument_type):
    addNewInstrument({"type": instrument_type})
    response = app.response_class(
        response=json.dumps({"type": instrument_type}),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/add/user/<firstName>/<lastName>', methods=["GET", "POST"])
def add_new_user(firstName, lastName):
    addNewUser({"firstName": firstName, "lastName": lastName})
    response = app.response_class(
        response=json.dumps({"firstName": firstName, "lastName": lastName}),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run()
