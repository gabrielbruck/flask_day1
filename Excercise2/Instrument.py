import json
import random
import string


class Instrument:
    def __init__(self, instrument):
        self.type = instrument["type"]
        self.user_id = "no user id"
        self.id = makerandomid()
        self.video = "no user video"

    def MakeAInstrumentDict(self):
        dict = json.dumps(self.__dict__)
        return dict


class User:
    def __init__(self, user):
        self.firstName = user["firstName"]
        self.lastName = user["lastName"]
        self.id = makerandomid()

    def MakeUserDict(self):
        dict = json.dumps(self.__dict__)
        return dict


def makerandomid(stringLength=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def GetInstruments():
    return list_instruments


def GetUser():
    return list_user


list_instruments = {}
list_user = {}


def addNewInstrument(instrument):
    instrum = Instrument(instrument)
    instrum_add = json.load(instrum.MakeAInstrumentDict())
    list_instruments[instrum_add['id']] = instrum_add


def addNewUser(user):
    newUser = User(user)
    user_add = json.load(newUser.MakeUserDict())
    list_user[user_add['id']] = user_add