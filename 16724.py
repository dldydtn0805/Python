import sys
input = sys.stdin.readline

def dfs(ci, cj, root):
    if visited[ci][cj]:
        return
    else:
        visited[ci][cj] = root
        di, dj = dir[arr[ci][cj]]
        ni, nj = ci + di, cj + dj
        if not visited[ni][nj]:
            dfs(ni, nj, root)
        else:
            if visited[ni][nj] != visited[ci][cj]:
                ans.remove(root)



dir = {
    'U' : [-1, 0], 'R' : [0, 1], 'D' : [1, 0], 'L' : [0, -1]
}
cnt = 0
N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]

visited = [[0 for _ in range(M)] for _ in range(N)]

ans = set()
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            ans.add((i, j))
            dfs(i, j, (i, j))

print(len(ans))
