class information:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduction(self):
        print(f"hey,myself {self.name} and my age is {self.age}")


persenal_info = information("Rayyan", 22)
persenal_info.introduction()
