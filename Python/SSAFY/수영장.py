import sys, heapq
from collections import deque
sys.stdin = open('input.txt')
def bfs(start):
    heap = []
    di = [1,1,3,12]
    heapq.heappush(heap, (0, start))
    while heap:
        nc, ni = heapq.heappop(heap)
        for k in range(4):
            if k == 0:
                nexti = ni + di[k]
                if nexti<13:
                    nextc = nc + cost[k]*arr[ni]
                else:
                    result.append(nextc)
                    continue
            else:
                nexti = ni + di[k]
                nextc = nc + cost[k]
                if nexti>12:
                    result.append(nextc)
                    continue
            # print(nexti, nextc)
            if nextc >= visited[nexti]:
                continue
            visited[nexti] = nextc
            heapq.heappush(heap, (nextc, nexti))

T = int(input())

for tc in range(1, T+1):
    cost = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    visited = [1e9]*13
    result = []
    bfs(0)
    print(visited)
    print(f'#{tc}', visited[len(visited)-1])

