import sys
input = sys.stdin.readline
import heapq

tc = 0
while True:
    tc += 1
    p = int(input())
    if p == 0:
        break
    else:
        heap = []
        for i in range(p):
            s, e = map(int, input().split())
            heapq.heappush(heap, [e, s])
        visited = [0 for _ in range(25)]
        while heap:
            nxt = heapq.heappop(heap)
            for ni in range(nxt[1], nxt[0]):
                if visited[ni] < 2:
                    visited[ni] += 1
                    break
        print(f'On day {tc} Emma can attend as many as {sum(visited)} parties.')
