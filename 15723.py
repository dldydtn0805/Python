import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(si):
    visited[si] = 1
    for ni in graph[si]:
        if not visited[ord(ni)-ord('a')]:
            dfs(ord(ni)-ord('a'))

n = int(input())
graph = [[] for _ in range(26)]

for _ in range(n):
    x, equal, y = input().rstrip().split()
    graph[ord(x)-ord('a')].append(y)

m = int(input())
for _ in range(m):
    visited = [0 for _ in range(26)]
    i, equal, j = input().rstrip().split()
    dfs(ord(i)-ord('a'))
    if visited[ord(j)-ord('a')]:
        print('T')
    else:
        print('F')
