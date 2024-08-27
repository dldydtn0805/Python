import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    while queue:
        if len(ans) >= K:
            return
        ci, value = queue.popleft()
        for ni in [ci+value, ci-value]:
            if 0 <= ni <= L:
                if ni not in visited:
                    ans.append(value)
                    visited.add(ni)
                    queue.append([ci, value+1])


L, N, K = map(int, input().split())
arr = list(map(int, input().split()))
queue = deque()
visited = set()
ans = []
for ele in arr:
    visited.add(ele)
    queue.append([ele, 1])
    ans.append(0)
bfs()
ans.sort()
for i in range(K):
    print(ans[i])
