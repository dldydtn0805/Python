'''

출발 = 집, 맥주 한박스 ( 20병 )

편의점 = 맥주 한박스 리필 가능

50미터마다 맥주 한병 소모

맥주 부족하지 않게 도착할수 있으면

'''


import sys
from collections import deque
# sys.stdin = open('input.txt')

def bfs():
    si, sx, sy = graph.pop(0)
    visited[si] = 1
    queue.append((si, sx, sy))
    while queue:
        ci, cx, cy = queue.popleft()
        for di, dx, dy in graph:
            if abs(dx - cx) + abs(dy - cy) <= 1000:
                if not visited[di]:
                    visited[di] = visited[ci] + 1
                    queue.append((di, dx, dy))

T = int(input())
for tc in range(T):
    n = int(input())
    queue = deque()
    graph = []
    for i in range(n+2):
        x, y = map(int, input().split())
        graph.append((i, x, y))
    visited = [0]*(n+2)
    bfs()
    if visited[len(visited)-1]:
        print('happy')
    else:
        print('sad')