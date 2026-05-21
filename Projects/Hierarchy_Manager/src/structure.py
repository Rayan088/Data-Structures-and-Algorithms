import random

class Structure:
    def __init__(self, position, Id=None):
        self.position = position
        self.children = []

        if Id is None:
            randomId = str(random.randint(0, 9999)).zfill(4)
            self.Id = randomId
        else:
            self.Id = Id