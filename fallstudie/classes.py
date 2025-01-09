# This is a function
def print_something(something):
    print(something)


class House:
    def __init__(self, color: str, width: int, depth: int, num_floors=3):
        self.color = color 
        self.num_floors = num_floors
        self.width = width
        self.depth = depth

    # this is a method
    def print_info(self):
        print(f"Color: {self.color}, Area: {self.width*self.depth}, Floors: {self.num_floors}")
        

h1 = House("green", 9, 6)
h1.print_info()

h2 = House("red", 10, 5)
h2.print_info()
