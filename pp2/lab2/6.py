n = int(input())
nums = list(map(int, input().split()))
a = nums[0]
for i in nums:
    if i > a:
        a = i
print(a)