#1 
def sum_nums(*a):
    print(sum(a))

sum_nums(1, 2, 3)


#2 
def max_num(*a):
    print(max(a))

max_num(5, 2, 9)


#3 
def count_nums(*a):
    print(len(a))

count_nums(10, 20, 30, 40)


#4 
def show(**info):
    for k, v in info.items():
        print(k, ":", v)

show(name="Timur", age=18)


#5
def get_city(**info):
    print(info.get("city", "No city"))

get_city(city="Timur")
get_city(name="Miras")
