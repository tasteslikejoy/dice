import random


class Dice:
    def __init__(self, sides=12):
        self.sides = sides
        self.value = 1

    def roll(self): # Возвращает кортеж, а нужно возвращать self.value и оно должно меняться
        return random.randint(1, self.sides), self.value

    # def get_image_path(self):
    #     return f'./images/dice_{self.value}.png'
