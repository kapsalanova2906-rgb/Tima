#1
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s = Student("Timur", "A")
print(s.name, s.grade)


#2
class Person:
    def __init__(self, name):
        self.name = name

class Worker(Person):
    def __init__(self, name, job):
        super().__init__(name)
        self.job = job

w = Worker("Timur", "Developer")
print(w.name, w.job)


#3
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, year):
        super().__init__(brand)
        self.year = year

c = Car("Toyota", 2020)
print(c.brand, c.year)


#4
class Account:
    def __init__(self, owner):
        self.owner = owner

class BankAccount(Account):
    def __init__(self, owner, balance):
        super().__init__(owner)
        self.balance = balance

a = BankAccount("Timur", 5000)
print(a.owner, a.balance)


#5
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

d = Dog("Timur", "Labrador")
print(d.name, d.breed)
