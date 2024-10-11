import sys

N, M = map(int, sys.stdin.readline().split())
visited = [[0] * (M + 1) for _ in range(N + 1)]
answer = 0

def dfs(cnt):
    global answer
    if cnt == N * M:
        answer += 1
        return

    y = cnt // M + 1
    x = cnt % M + 1

    dfs(cnt + 1)
    if visited[y - 1][x] == 0 or visited[y][x - 1] == 0 or visited[y - 1][x - 1] == 0:
        visited[y][x] = 1
        dfs(cnt + 1)
        visited[y][x] = 0


dfs(0)
print(answer)
