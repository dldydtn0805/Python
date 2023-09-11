import sys, heapq
input = sys.stdin.readline
n, k = map(int, input().split())
heap = [[] for _ in range(11)]
for _ in range(n):
    p, w = map(int, input().split())
    heapq.heappush(heap[p-1], -w)
for _ in range(k):
    for i in range(11):
        if heap[i] and heap[i][0] + 1 < 0:
            x = heapq.heappop(heap[i])
            heapq.heappush(heap[i], x+1)
result = 0
for i in range(11):
    if heap[i]:
        x = -heap[i][0]
        result += x
print(result)