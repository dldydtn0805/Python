import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(si, sj):
    visited[si][sj] = 1
    for di, dj in [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]:
        ni, nj = si+di, sj+dj
        if 0<=ni<h and 0<=nj<w:
            if not visited[ni][nj]:
                if islands[ni][nj] == 1:
                    dfs(ni, nj)

test_case = True

while test_case:
    w, h = map(int, input().split())
    visited = [[0 for _ in range(w)] for _ in range(h)]
    if w == 0 and h == 0:
        test_case = False
        break
    islands = [list(map(int, input().split())) for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j]:
                if islands[i][j] == 1:
                    ans += 1
                    dfs(i, j)
    print(ans)
