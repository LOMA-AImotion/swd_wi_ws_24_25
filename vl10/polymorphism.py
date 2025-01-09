class Pet:
    def __init__(self, name):
        self.name = name
        
    def sound(self):
        pass 
    
    def greet(self):
        print(f"Hi, I'm {self.name}, my sound is {self.sound()}")
        
    
class Cat(Pet):
    def __init__(self):
        super().__init__("cat")

    def sound(self):
        print("Miau")
    
class Dog(Pet):
    def __init__(self):
        super().__init__("dog")

    def sound(self):
        print("Bark")
 
def let_pets_make_sound(all_pets: list[Pet]):
    for p in all_pets:
        p.sound()
    
c = Cat()
c.sound()

d = Dog()
d.sound()
