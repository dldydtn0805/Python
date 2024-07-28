import sys
input = sys.stdin.readline
import heapq
def dijkstra(si):
    heap = []
    heapq.heappush(heap, (-1*1e9, si))
    distance = [0 for _ in range(N)]
    distance[si] = 1e9
    while heap:
        cw, ci = heapq.heappop(heap)
        cw = -1 * cw
        if cw < distance[ci]:
            continue
        for nw, ni in adjacent_list[ci]:
            next_distance = min(cw, nw)
            if next_distance > distance[ni]:
                distance[ni] = next_distance
                heapq.heappush(heap, (-1*next_distance, ni))
    return distance
N, M = map(int, input().split())
s, e = map(int, input().split())
adjacent_list = [[] for _ in range(N)]

ans = 0
s -= 1
e -= 1
for _ in range(M):
    h1, h2, k = map(int, input().split())
    h1 -= 1
    h2 -= 1
    adjacent_list[h1].append((k, h2))
    adjacent_list[h2].append((k, h1))

print(dijkstra(s)[e])
