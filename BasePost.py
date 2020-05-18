class BasePost():
    def __init__(self, dict_obj):
        self.userId = dict_obj['userId']
        self.id = dict_obj['id']
        self.title = dict_obj['title']
        self.body = dict_obj['body']


