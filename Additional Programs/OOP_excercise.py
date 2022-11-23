class Vehicle:
    def __init__(self, maxspeed, colour):

        self.maxspeed = maxspeed
        self.colour = colour

    def increment_speed(self):
        self.maxspeed += 10

    def change_colour(self):
        self.colour = "green"

    def my_car(self):
        print(f"My vehicle has a max speed of {self.maxspeed}mph and is {self.colour}")

car = Vehicle(90, "red")

car.maxspeed
car.colour
car.increment_speed()
car.change_colour()
car.my_car()

class Bus(Vehicle):
    def __init__(self, maxspeed, colour):
        super().__init__(maxspeed, colour)

bus = Bus(70, "red")

bus.increment_speed()
bus.change_colour()
bus.my_car()