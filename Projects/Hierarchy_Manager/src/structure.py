import random

class Employee:
    def __init__(self, position, head, Id=None):
        self.head = head
        self.position = position
        self.children = []

        if Id is None:
            randomId = str(random.randint(0, 9999)).zfill(4)
            self.Id = randomId
        else:
            self.Id = Id

    #Initialiser method