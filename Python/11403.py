import sys
input = sys.stdin.readline
from collections import deque
def bfs(s):
    queue = deque()
    visited = [0 for _ in range(N)]
    queue.append(s)
    while queue:
        cur = queue.popleft()
        for i in range(len(arr[cur])):
            if arr[cur][i] == 1:
                if not visited[i]:
                    visited[i] = 1
                    queue.append(i)
    print(*visited)
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    bfs(i)
