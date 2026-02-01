n = int(input())
arr = [input().strip() for _ in range(n)]

first_occurrence = {}

# запоминаем первый индекс каждой строки
for i, s in enumerate(arr):
    if s not in first_occurrence:
        first_occurrence[s] = i + 1  # индексация с 1

# сортируем строки в лексикографическом порядке
for s in sorted(first_occurrence):
    print(s, first_occurrence[s])
