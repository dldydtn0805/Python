import sys
# sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)
from collections import deque
def bfs():
    while queue:
        a, b = queue.popleft()
        for k in range(4):
            ni = a + di[k]
            nj = b + dj[k]
            if 0<= ni <n and 0<=nj<m:
                if visited[ni][nj] == -1:
                    queue.append((ni,nj))
                    # 선입 선출이므로 해당 자리에 들어갈 수 있는 가장 높은 안전 거리 값이 작성된다
                    visited[ni][nj] = visited[a][b] + 1


T = int(input())
for tc in range(1, T+1):
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    n, m = map(int, input().split())
    s = 0
    visited = [[-1]*m for _ in range(n)]
    queue = deque()
    for i in range(n):
        tmp = input()
        for j in range(m):
            if tmp[j] == 'W':
                queue.append((i, j))
                visited[i][j] = 0

    bfs()
    for i in range(n):
        for j in range(m):
            s += visited[i][j]
    # print(visited)
    print(f'#{tc}',s)