#1
def greet():
    print("Hello, student!")

greet()


#2
def add(a, b):
    print(a + b)

add(3, 5)


#3
def square(x):
    return x * x

print(square(4))


#4
def print_list(items):
    for item in items:
        print(item)

print_list([1, 2, 3])

#5
def power(base, exponent=2):
    print(base ** exponent)

power(3)      # 3^2
power(2, 5)   # 2^5
