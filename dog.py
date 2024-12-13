import random
import time

class Pet:
    def __init__(self, name, species="Cat"):
        self.name = input()
        self.health = 100
        self.hunger = 0
        self.happiness = 100

    def feed(self):
        if self.hunger > 0:
            print(f"{self.name} їсть...")
            self.hunger = max(0, self.hunger - 20)
            self.happiness = min(100, self.happiness + 10)
        else:
            print(f"{self.name} не голодний!")

    def sleep(self):
        print(f"{self.name} спить...")
        self.health = min(100, self.health + 10)

    def play(self):
        if self.happiness > 20:
            print(f"{self.name} грає...")
            self.hunger += 10
            self.happiness = min(100, self.happiness + 20)
        else:
            print(f"{self.name} я втомився")
#нажаль гру я не зміг реалізувати але постарався зробити певні дії та класи які б мали виконувати котик чи собака



