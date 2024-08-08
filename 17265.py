import sys
input = sys.stdin.readline
def dfs(ci, cj, string):
    if ci == N-1 and cj == N-1:
        tmp = int(string[0])
        for i in range(1, len(string)):
            if string[i].isnumeric():
                if string[i-1] == '*':
                    tmp *= int(string[i])
                elif string[i-1] == '+':
                    tmp += int(string[i])
                elif string[i-1] == '-':
                    tmp -= int(string[i])
        ans.add(tmp)
        return
    for di, dj in [[1,0],[0,1]]:
        ni, nj = ci+di, cj+dj
        if 0<=ni<N and 0<=nj <N:
            if not visited[ni][nj]:
                visited[ni][nj] = 1
                dfs(ni, nj, string+arr[ni][nj])
                visited[ni][nj] = 0


N = int(input())
arr = [list(input().rstrip().split()) for _ in range(N)]
ans = set()
visited = [[0 for _ in range(N)] for _ in range(N)]
visited[0][0] = 1
dfs(0, 0, arr[0][0])
print(max(ans), min(ans))
