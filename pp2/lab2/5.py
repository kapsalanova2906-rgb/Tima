a = int(input())
s = 0
while(True):
    if 2 ** s == a:
        print("YES")
        break
    elif 2 ** s > a:
        print("NO")
        break
    s += 1
    
    