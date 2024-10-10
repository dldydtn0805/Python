import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
adj_list = [set() for _ in range(N+1)]
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(len(arr)-1):
        adj_list[arr[j]].add(i+1)
        adj_list[i+1].add(arr[j])
M = int(input())
users = list(map(int, input().split()))
visited = [-1 for _ in range(N+1)]
queue = deque(users)
for user in users:
    visited[user] = 0
def bfs():
    tmp = deque()
    while queue:
        ci = queue.popleft()
        for ni in adj_list[ci]:
            cnt = 0
            if visited[ni] == -1:
                for mi in adj_list[ni]:
                    if visited[mi] != -1:
                        cnt += 1
                if 2*cnt < len(adj_list[ni]):
                    continue
                tmp.append(ni)
        if not queue:
            while tmp:
                ti = tmp.popleft()
                visited[ti] = visited[ci]+1
                queue.append(ti)
bfs()
print(*visited[1:])

