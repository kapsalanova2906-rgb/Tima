#1
class Flyer:
    def fly(self):
        print("Flying")

class Swimmer:
    def swim(self):
        print("Swimming")

class Duck(Flyer, Swimmer):
    pass

d = Duck()
d.fly()
d.swim()


#2
class Runner:
    def run(self):
        print("Running")

class Jumper:
    def jump(self):
        print("Jumping")

class Athlete(Runner, Jumper):
    pass

a = Athlete()
a.run()
a.jump()


#3
class Speaker:
    def speak(self):
        print("Speaking")

class Writer:
    def write(self):
        print("Writing")

class Person(Speaker, Writer):
    def __init__(self, name):
        self.name = name

p = Person("Timur")
p.speak()
p.write()


#4
class Charger:
    def charge(self):
        print("Charging")

class Player:
    def play(self):
        print("Playing music")

class Phone(Charger, Player):
    pass

ph = Phone()
ph.charge()
ph.play()


#5
class Reader:
    def read(self):
        print("Reading")

class Gamer:
