import ujson

class Item(object):
    """
    """
    def __init__(self, **args):
        self.args = args

    def to_json(self):
        return ujson.dumps(self.args)
