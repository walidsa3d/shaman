class Movie(object):

    def __init__(self):
        self.title = ""
        self.id = ""
        self.plot = ""
        self.year = ""

    def __str__(self):
        return str(self.__dict__)
