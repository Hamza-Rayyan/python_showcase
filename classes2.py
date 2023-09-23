class Person:
    def __init__(self, name):
        self.name = name        
    def talk(self):
        print(f"hey, i am {self.name} and how are you")
        

person = Person("hamza")
person.talk()

        
        