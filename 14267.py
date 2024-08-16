import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(si, w):
    ans[si] += w
    w = ans[si]
    for ni in adj_list[si]:
        dfs(ni, w)

n, m = map(int, input().split())
arr = list(map(int,input().split()))
adj_list = [[] for _ in range(n)]
for i in range(1, len(arr)):
    adj_list[arr[i]-1].append(i)
ans = [0 for _ in range(n)]
for _ in range(m):
    i, w = map(int, input().split())
    ans[i-1] += w
dfs(0, 0)
print(*ans)
