

class Store(object):
    def __init__(self, name, url_prifex):
        self.name = name
        self.url_prifex = url_prifex

    def __repr__(self):
        return "<Store {}>".format(self.name)