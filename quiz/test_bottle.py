class Bottle:
    def __init__(self, content, type):
        self.content = content
        self.type = type

bottle1 = Bottle("empty", "PET")
bottle2 = Bottle("water", "PET")

bottle3 = bottle1