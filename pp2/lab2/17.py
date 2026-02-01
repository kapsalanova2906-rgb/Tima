n = int(input())
cnt = {}

for _ in range(n):
    num = input().strip()
    cnt[num] = cnt.get(num, 0) + 1

answer = 0
for v in cnt.values():
    if v == 3:
        answer += 1

print(answer)
