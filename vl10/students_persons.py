class Person:
    
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        print(f"Hello, I am {self.name}")
        
        
class Student(Person):
    
    def __init__(self, name, mat_id):
        super().__init__(name)
        
        self.mat_id = mat_id
    
    def greet(self):
        print(f"Hello, I am {self.name}, and my Mat ID is {self.mat_id}")


p = Person("Caro")
p.greet()
s = Student("Frank", 123456)
s.greet()

