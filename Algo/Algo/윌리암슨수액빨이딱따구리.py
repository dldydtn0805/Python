import sys
from collections import deque
# sys.stdin = open('input.txt')
input = sys.stdin.readline
def bfs():
    while q:
        i, j = q.popleft()
        # 만약 음식일때, 방문했다면 해당 영역이 가장 빠르게 먹을수있는 음식이므로 그때의 거리를 반환해준다
        if food[i][j] and visited[i][j]:
            return visited[i][j]
        # 상하좌우 움직이면서 visited가 방문할수있는 영역일때 q에 해당 위치를 넣어주고 거리를 1 더해준다
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            ni, nj = i + di, j + dj
            if 0<=ni<n and 0<=nj<m:
                if visited[ni][nj] == 0:
                    q.append((ni,nj))
                    visited[ni][nj] = visited[i][j]+1

n, m = map(int, input().strip().split())
arr = [[0] for _ in range(n)]
# 방문 가능한 영역인지 체크하는 visited와 음식인지를 체크하는 food 선언
visited = [[-1]*m for _ in range(n)]
food = [[0]*m for _ in range(n)]
# bfs를 위한 q
q = deque()

for i in range(n):
    # temp에 순차적으로 입력을 받는데,
    # 만약 해당 영역이 1이 아닐때는 visited를 0으로 바꿔서 이동 가능하게 해주고
    # 해당 영역이 2일때는 q에 넣어서 시작점으로 설정해주고
    # 해당 영역이 3,4,5 중 하나일때는 food를 1로 바꿔서 음식임을 표시해준다
    temp = list(map(int,input().strip()))
    for j in range(m):
        if temp[j] != 1:
            visited[i][j] = 0
        if temp[j] == 2:
            q.append((i,j))
        if temp[j] in [3,4,5]:
            food[i][j] = 1

result = (bfs())

if result:
    print('TAK')
    print(result)
else:
    print('NIE')
