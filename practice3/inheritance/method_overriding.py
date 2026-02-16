#1
class Animal:
    def speak(self):
        print("Animal sound")

class Cat(Animal):
    def speak(self):
        print("Meow")

c = Cat()
c.speak()


#2
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof")

d = Dog()
d.speak()


#3
class Animal:
    def speak(self):
        print("Animal sound")

class Bird(Animal):
    def speak(self):
        print("Tweet")

b = Bird()
b.speak()


#4
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "sound")

class Cat(Animal):
    def speak(self):
        print(self.name, "says Meow")

c = Cat("Timur")
c.speak()


#5
class Animal:
    def speak(self):
        print("Animal sound")

class Cat(Animal):
    def speak(self):
        super().speak()
        print("Meow")

c = Cat()
c.speak()
