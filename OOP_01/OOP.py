"""OOP - object oriented programming
An Object is an instance of a class --Important
In order to create an object, we will have to create a class
An object can have an atrribute (is/has) and a method(Actions)
"""
class Car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color


    def drive(self):
        print("This car is driving")

    def stop(self):
        print("This car is stopped")


car_1  = Car("Ford", "Mustang",2021, "Red")
print(car_1.color)
car_1.drive()
car_1.stop()


