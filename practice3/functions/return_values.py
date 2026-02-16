#1
def full_name(first, last):
    return first + " " + last

name = full_name("Timur", "Abu")
print(name)


#2
def is_positive(x):
    return x > 0

print(is_positive(5))
print(is_positive(-2))


#3
def make_squares(nums):
    squares = []
    for n in nums:
        squares.append(n * n)
    return squares

result = make_squares([1, 2, 3, 4])
print(result)


#4
def max_of_two(a, b):
    if a > b:
        return a
    return b

print(max_of_two(10, 7))
print(max_of_two(3, 9))


#5
def min_max(nums):
    return min(nums), max(nums)

mn, mx = min_max([4, 1, 9, 2])
print(mn, mx)
