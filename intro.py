class Info():
    def __init__(self, name):
        self.name = name           
    def talk(self):
        print(f"hey myself {self.name} how are you")
        
        
info = Info(input())
info.talk()
        