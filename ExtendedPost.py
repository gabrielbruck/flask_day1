from BasePost import BasePost
import datetime


class ExtendedPost(BasePost):
    def __init__(self, post_obj):
        super().__init__(post_obj)
        self.createdAt = str(datetime.datetime.now())
