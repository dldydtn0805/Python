import sys
import heapq

input = sys.stdin.readline

N = int(input())
lectures = []

for _ in range(N):
    n, s, e = map(int, input().split())
    lectures.append((s, e))

lectures.sort(key=lambda x: x[0])
rooms = []
max_rooms = 0

for start, end in lectures:
    while rooms and rooms[0] <= start:
        heapq.heappop(rooms)
    heapq.heappush(rooms, end)
    max_rooms = max(max_rooms, len(rooms))
print(max_rooms)
