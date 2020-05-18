from ExtendedPost import ExtendedPost
import json


class JsonablePost(ExtendedPost):
    def __init__(self, post):
        super().__init__(post)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

