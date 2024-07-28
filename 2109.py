import sys
import heapq
input = sys.stdin.readline

N = int(input())
day = []
visited = [0 for _ in range(10001)]
for i in range(N):
    p, d = map(int, input().split())
    heapq.heappush(day, (-p, d, p))
ans = 0
while day:
    a, b, c = (heapq.heappop(day))
    for i in range(b-1, -1, -1):
        if not visited[i]:
            visited[i] = c
            break
print(sum(visited))

