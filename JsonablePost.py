from ExtendedPost import ExtendedPost
import json


class JsonablePost(ExtendedPost):
    def __init__(self, post):
        super().__init__(post)

    def format_to_json(self):
        jsonObj = json.dumps(self.__dict__)
        return jsonObj
