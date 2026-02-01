n = int(input())
c = 0
nums = list(map(int, input().split()))
for i in range(n):
    if nums[i] > 0:
        c += 1
print(c)
