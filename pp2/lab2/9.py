n = int(input())
nums = list(map(int, input().split()))
a = nums[0]
b = nums[0]
for i in nums:
    if i > a:
        a = i
    if i < b:
        b = i

for i in range(n):
    if nums[i] == a:
        nums[i] = b
print(*nums)