class Animal():
    alive  = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("this animal is running")

class Fish(Animal):
    def swim(self):
        print("this animal is swimming")

class Hawk(Animal):
    def fly(self):
        print("this animal is flying")

rabbit  = Rabbit()
fish = Fish()
hawk = Hawk()

# print(rabbit.alive)
# fish.eat()
# hawk.sleep()

rabbit.run()

fish.swim()
hawk.fly()