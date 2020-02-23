class Car():
    def __init__(self, name):
        self.name = name
    
    def description(self):
        print(self.name + " is handsome")

class ElectricCar(Car):
    def oh(self):
        print('jinhuale')
