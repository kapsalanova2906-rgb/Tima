#1
def introduce(name, age):
    print("Name:", name, "Age:", age)

introduce("Miras", 18)


#2
def power(number, exp=2):
    return number ** exp

print(power(5))
print(power(5, 3))

#3
def show_info(city, country):
    print("City:", city, "Country:", country)

show_info(country="Kazakhstan", city="Almaty")


#4
def total_sum(*numbers):
    s = 0
    for n in numbers:
        s += n
    print("Sum:", s)

total_sum(1, 2, 3, 4, 5)


#5
def print_profile(**data):
    for key, value in data.items():
        print(key + ":", value)

print_profile(name="Miras", age=18, hobby="football")
