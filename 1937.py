import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(ci, cj):
    global ans
    tmp = 0
    for di, dj in [[-1,0],[0,1],[1,0],[0,-1]]:
        ni, nj = ci + di, cj + dj
        if 0<=ni<n and 0<=nj<n:
            if arr[ci][cj] > arr[ni][nj]:
                if not visited[ni][nj]:
                    depth = dfs(ni, nj)
                    tmp = max(depth, tmp)
                else:
                    tmp = max(visited[ni][nj]+1, tmp)
    if tmp:
        visited[ci][cj] = tmp
        return visited[ci][cj] + 1
    else:
        visited[ci][cj] = 1
        return visited[ci][cj] + 1

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[0 for _ in range(n)] for _ in range(n)]
ans = 0
start = []
for i in range(n):
    for j in range(n):
        dfs(i, j)

for col in visited:
    for row in col:
        ans = max(row, ans)

print(ans)
