import sys
input = sys.stdin.readline
from collections import deque
def dfs(arr):
    tmp = arr.popleft()
    if not arr:
        print(1)
        exit()
    visited[tmp] = 1
    for _ in range(len(adj_list[tmp])):
        if arr[0] in adj_list[tmp] and visited[arr[0]] == 0:
            dfs(arr)

N = int(input())
adj_list = [[] for _ in range(N+1)]
for _ in range(N-1):
    start, end = map(int, input().split())
    adj_list[start].append(end)
    adj_list[end].append(start)
arr = deque(list(map(int, input().split())))
visited = [0 for _ in range(N+1)]
if arr[0] != 1:
    print(0)
    exit()
dfs(arr)
print(0)
