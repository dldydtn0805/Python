import sys, heapq
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
arr = []
for _ in range(N):
    P, Q = map(int, input().split())
    arr.append([P, Q])
arr.sort()

heap = []
heapq.heappush(heap, [arr[0][1], 1])
ans = defaultdict(int)
visited = []
ans[1] = 1

for i in range(1, len(arr)):
    while heap and heap[0][0] < arr[i][0]:
        end_room = heapq.heappop(heap)[1]
        heapq.heappush(visited, end_room)
    else:
        if visited:
            next_room = heapq.heappop(visited)
            heapq.heappush(heap, [arr[i][1], next_room])
            ans[next_room] += 1
        else:
            heapq.heappush(heap, [arr[i][1], len(heap)+1])
            ans[len(heap)] += 1



print(len(ans))
for i in range(1, len(ans)+1):
    print(ans[i], end= ' ')

