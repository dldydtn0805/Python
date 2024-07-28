import sys
input = sys.stdin.readline
from collections import defaultdict
N = int(input())
ans = defaultdict(int)
for _ in range(N):
    alphabets = input().rstrip()
    cnt = 0
    for i in range(len(alphabets)-1, -1, -1):
        ans[alphabets[i]] += 10**cnt
        cnt += 1

res = []
for value in ans.values():
    res.append(value)
answer = 0
res.sort(reverse=True)
tmp = 9
for response in res:
    answer += response * tmp
    tmp -= 1
print(answer)
