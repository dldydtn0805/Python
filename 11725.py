import sys
input = sys.stdin.readline
from collections import deque

def bfs(start_node):
    visited = [[0, 0]for _ in range(n)]
    queue = deque()
    visited[start_node][0] = start_node
    visited[start_node][1] = 1
    queue.append(start_node)
    while queue:
        current_node = queue.popleft()
        for next_node in arr[current_node]:
            if not visited[next_node][1]:
                visited[next_node][0] = current_node
                visited[next_node][1] = visited[current_node][1] + 1
                queue.append(next_node)
    return visited

n = int(input())
arr = [[] for _ in range(n)]
for _ in range(n-1):
    node_1, node_2 = map(int, input().split())
    node_1 -= 1
    node_2 -= 1
    arr[node_1].append(node_2)
    arr[node_2].append(node_1)
res = (bfs(0))
for i in range(1, len(res)):
    print(res[i][0]+1)
