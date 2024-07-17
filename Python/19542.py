import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(si, pre):
    check = 0
    for ni in adj[si]:
        if ni != pre:
            check = max(check, dfs(ni, si))
    if check >= D:
        ans[0] += 1
    return check + 1

N, S, D = map(int, input().split())
adj = [[] for _ in range(N)]
ans = [0]
for _ in range(N-1):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    adj[x].append(y)
    adj[y].append(x)
S -= 1
dfs(S, 0)
print(max(0, 2*(ans[0]-1)))
