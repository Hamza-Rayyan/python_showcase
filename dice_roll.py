import random


class Dice:
    def roll(self):
        for i in range(1):
            x = random.randint(1,6)
            y = random.randint(1,6)
            return x , y


dice = Dice()
print(dice.roll())
        

        