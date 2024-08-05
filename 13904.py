import sys
input = sys.stdin.readline
import heapq
N = int(input())
arr = [[] for _ in range(1001)]
for _ in range(N):
    d, w = map(int, input().split())
    arr[d].append(w)

max = 0
tmp = []
for i in range(1000, 0, -1):
    if arr[i]:
        for j in range(len(arr[i])):
            heapq.heappush(tmp, -arr[i][j])
    if tmp:
        max_v = -heapq.heappop(tmp)
        max += max_v
print(max)
