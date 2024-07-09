import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    ans = 0
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for dx, dy in [[-1,0],[0,1],[1,0],[0,-1]]:
            nx, ny = x + dx, y + dy
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    ans += 1
    return ans + 1

# 전에 했던 물놀이를 가자와 다른 점은 여기서는 그래프와 방문처리를 각각 했다는 점이다
# 이 문제는 쓰레기가 있는 영역과 쓰레기가 없는 영역이 구분이 되어있다는 점이다
# 방문처리를 True와 False로 해서 연결되어있는 영역별로 구성될수있는 가장 큰 사이즈를 각각 구한다
# 그리고 가장 큰 사이즈를 출력하면 된다

n, m, k = map(int, input().split())
graph = [[0]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

max_v = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            max_v = max(max_v, bfs(i,j))

print(max_v)