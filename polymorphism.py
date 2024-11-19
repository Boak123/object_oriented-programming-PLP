# Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving", while Plane.move() prints "Flying").
class Animal:

    def move(self):
        return "Animal is moving"

class Bird:
    
    def move(self):
        return "Bird is flying"


class Dog:

    def move(self):
        return "Dog is running"

for animal in (Animal(), Bird(), Dog()):
    print(animal.move())