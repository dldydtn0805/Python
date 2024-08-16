import sys, math
input = sys.stdin.readline
from collections import defaultdict
N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]
dict = defaultdict(set)

for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        i1, j1 = arr[i]
        i2, j2 = arr[j]
        if i1 == i2:
            if j1 < j2:
                dict[(j1, j2)].add(i1)
            else:
                dict[(j2, j1)].add(i1)
ans = 0
for value in dict.values():
    ans += math.comb(len(value), 2)
print(ans)
