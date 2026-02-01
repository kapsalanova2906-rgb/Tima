n = int(input())
a = list(map(int, input().split()))

cnt = {}

for x in a:
    if x in cnt:
        cnt[x] += 1
    else:
        cnt[x] = 1

max_freq = 0
answer = None

for x in cnt:
    if cnt[x] > max_freq or (cnt[x] == max_freq and x < answer):
        max_freq = cnt[x]
        answer = x

print(answer)
