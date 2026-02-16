#1
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)


#2
numbers = [1, 2, 3, 4, 5, 6]
odds = list(filter(lambda x: x % 2 != 0, numbers))
print(odds)


#3
numbers = [1, 2, 3, 4, 5, 6]
greater_than_3 = list(filter(lambda x: x > 3, numbers))
print(greater_than_3)


#4
names = ["Timur", "Ali", "Sanzhar", "Dana"]
only_timur = list(filter(lambda x: x == "Timur", names))
print(only_timur)


#5
words = ["cat", "elephant", "dog", "lion"]
long_words = list(filter(lambda w: len(w) >= 4, words))
print(long_words)
