arr = input().split()
n = int(input())

def cycle(arr, n):
    for _ in range(n):
        for x in arr:
            yield x

first = True
for v in cycle(arr, n):
    if not first:
        print(" ", end="")
    print(v, end="")
    first = False