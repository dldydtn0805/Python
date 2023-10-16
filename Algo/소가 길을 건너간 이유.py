"""
목초지 정사각형 n x n

인접한 목초지는 자유롭게 건널수 있다

k마리의 소가 농장에 있다, 각 소는 서로 다른 목초지에 있다

어떤 두 소는 길을 건너지 못하면 만나지 못한다

(소의 위치를 기준으로 bfs를 돌리는데, 그 과정에서 길을 지났으면 카운트를 하나 더해준다)

길을 지났는지 확인하는 법은 ?

건너지 않으면 못만나는 경우 = 길을 막아놨는데도 만나는 경우를 세고, 그 나머지를 구하면 된다



"""
from itertools import combinations
import sys
sys.setrecursionlimit(10**6)
sys. stdin = open('input.txt')

def dfs(i, j, temp):
    global flag, route
    visited[i][j] = 1
    if i == ei and j == ej:
        print(temp)
        return
    for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
        ni, nj = i + di, j + dj
        if 0<=ni<n and 0<=nj<n:
            if not visited[ni][nj]:
                for t in roads:
                    t_r1, t_c1, t_r2, t_c2 = t
                    if i == t_r1 and j == t_c1 and ni == t_r2 and nj == t_c2:
                        flag = 1
                dfs(ni,nj, temp + ' ' + str(ni) + ' ' + str(nj))
                visited[ni][nj] = 0

n, k, r = map(int, input().split())
graph = [[0]*n for _ in range(n)]
roads = []
cows = []
for _ in range(r):
    r1, c1, r2, c2 = map(int, input().split())
    roads.append((r1-1,c1-1,r2-1,c2-1))

for _ in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1
    cows.append((x-1,y-1))

cnt = 0
targets = list(combinations(cows, 2))
for target in targets:
    si, sj = target[0]
    ei, ej = target[1]
    flag = 0
    route = set()
    visited = [[0]*n for _ in range(n)]
    dfs(si, sj, str(si) + ' ' + str(sj))
    print(flag)


