import sys
input = sys.stdin.readline

from collections import defaultdict

def dfs(start, prev, idx):
    if prev == -1:
        visited[start] = ''
    else:
        visited[start] = visited[prev]+'*+/'[idx]
    if start == t:
        ans.add(visited[start])
    nxt = [start*start, start+start, 1]
    for ni in range(3):
        if not visited[nxt[ni]] and nxt[ni] <= t:
            dfs(nxt[ni], start,  ni)
            visited[nxt[ni]] = ''


s, t = map(int, input().split())
ans = set()
if s == t :
    print(0)
elif t == 0:
    print('-')
elif t == 1:
    print('/')
else:
    visited = defaultdict(str)
    for i in range(3):
        dfs(s, -1, i)
    if ans:
        print((sorted(list(ans), key=lambda x : [len(x), x]))[0])
    else:
        print(-1)
