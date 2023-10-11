"""
목초지 정사각형 n x n

인접한 목초지는 자유롭게 건널수 있다

k마리의 소가 농장에 있다, 각 소는 서로 다른 목초지에 있다

어떤 두 소는 길을 건너지 못하면 만나지 못한다

(소의 위치를 기준으로 bfs를 돌리는데, 그 과정에서 길을 지났으면 카운트를 하나 더해준다)

길을 지났는지 확인하는 법은 ?


"""
from collections import deque
from itertools import combinations
import sys
sys. stdin = open('input.txt')

def bfs(si, sj):
    visited[si][sj] = 1
    queue = deque()
    queue.append((si,sj, str(si)+ ' ' +str(sj)))
    while queue:
        ci, cj, c_path = queue.popleft()
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            ni, nj = ci + di, cj + dj
            if 0<=ni<n and 0<=nj<n:
                if not visited[ni][nj]:
                    visited[ni][nj] = visited[ci][cj] + 1
                    c_path = c_path + ' ' + str(ni) + ' ' + str(nj)
                    queue.append((ni,nj, c_path))
                    if ni == ei and nj == ej:
                        return c_path

n, k, r = map(int, input().split())
graph = [[0]*n for _ in range(n)]
roads = []
cows = []

for _ in range(r):
    r1, c1, r2, c2 = map(int, input().split())
    temp1 = (str(r1 - 1) + ' ' + str(c1 - 1) + ' ' +  str(r2 - 1) + ' ' + str(c2 - 1))
    temp2 = (str(r2 - 1) + ' ' + str(c2 - 1) + ' ' +  str(r1 - 1) + ' ' + str(c1 - 1))
    roads.append(temp1)
    roads.append(temp2)
for _ in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1
    cows.append((x-1,y-1))

cnt = 0
targets = list(combinations(cows, 2))
for target in targets:
    si, sj = target[0]
    ei, ej = target[1]
    visited = [[0]*n for _ in range(n)]
    result = bfs(si, sj)
    print(roads)
    print(result)
    for m in range(len(result)):
        if m % 2 == 0:
            if result[m:m+7] in roads:
                cnt += 1
print(cnt)

