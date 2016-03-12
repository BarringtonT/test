import sys


class CoffeeMachine:
    name = ""
    bean = 0
    water = 0

    def __init__(self, name, bean, water):
        self.name = name
        self.bean = bean
        self.water = water

    def addBean(self):
        self.bean = self.bean + 1

    def addWater(self):
        self.water = self.water + 1

    # removes items
    def remBean(self):
        self.bean = self.bean - 1

    def remWater(self):
        self.water = self.water - 1

    # Status print

    def machineStatus(self):
        print("Name = " + self.name)
        print("Bean = " + str(self.bean))
        print("Water = " + str(self.water))
