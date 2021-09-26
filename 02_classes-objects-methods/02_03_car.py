# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.
class Car:
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def __str__(self):
        return f"{self.model},{self.year}, {self.max_speed}"

    def increaseSpeed(self, speed):
        currentspeed = self.max_speed
        self.max_speed = currentspeed + speed

car1 = Car("Nissan", "1998", 200)
print(car1)
car1.increaseSpeed(40)
print(car1)





        