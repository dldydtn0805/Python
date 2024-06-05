import sys
input = sys.stdin.readline
from collections import deque
def bfs(start):
    visited = [0 for _ in range(N)]
    queue = deque()
    visited[start] = 1
    queue.append(start)
    while queue:
        cur = queue.popleft()
        for i in range(len(arr[cur])):
            if not visited[arr[cur][i]]:
                visited[arr[cur][i]] = 1
                queue.append(arr[cur][i])
    return visited
N, M = map(int, input().split())
arr = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    arr[a].append(b)
ans = []
for i in range(len(arr)):
    res = bfs(i)
    ans.append(res)
cnt = 0
for i in range(len(ans)):
    flag = True
    for j in range(len(ans[i])):
        if ans[i][j] == 0 and ans[j][i] == 0:
                flag = False
    if flag: cnt += 1
print(cnt)
