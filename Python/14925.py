import sys
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
visited = [[0 for _ in range(N)] for _ in range(M)]
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            if i == 0 or j == 0:
                visited[i][j] = 1
            else:
                visited[i][j] = min(visited[i-1][j], visited[i][j-1], visited[i-1][j-1]) + 1
L = 0
for i in range(M):
    for j in range(N):
        L = max(L, visited[i][j])
print(L)
