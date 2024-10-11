def dfs(depth):
    global answer
    if depth == N * M:
        answer += 1
        return
    ni = depth // M + 1
    nj = depth % M + 1
    dfs(depth + 1)
    if visited[ni - 1][nj] == 0 or visited[ni][nj - 1] == 0 or visited[ni - 1][nj - 1] == 0:
        visited[ni][nj] = 1
        dfs(depth + 1)
        visited[ni][nj] = 0

N, M = map(int, input().split())
visited = [[0] * (M + 1) for _ in range(N + 1)]
answer = 0

dfs(0)
print(answer)
