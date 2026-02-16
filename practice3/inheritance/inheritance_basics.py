#1
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    pass

d = Dog()
d.speak()


#2
class Animal:
    def speak(self):
        print("Some sound")

class Cat(Animal):
    def speak(self):
        print("Meow")

c = Cat()
c.speak()


#3
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "makes a sound")

class Dog(Animal):
    pass

d = Dog("Timur")
d.speak()


#4
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def run(self):
        print("Dog is running")

d = Dog()
d.speak()
d.run()


#5
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

d = Dog()
d.speak()
