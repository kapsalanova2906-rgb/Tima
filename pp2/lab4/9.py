n = int(input())

def powers(n):
    x = 1
    for _ in range(n + 1):
        yield x
        x *= 2

first = True
for v in powers(n):
    if not first:
        print(" ", end="")
    print(v, end="")
    first = False