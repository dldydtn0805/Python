import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V = int(input())
graph = [[] for _ in range(V+1)]

for v in range(1, V+1):
    information = list(map(int, input().split()))
    cnt_node = information[0]
    idx = 1
    while information[idx] != -1:
        adj_node, adj_cost = information[idx], information[idx + 1]
        graph[cnt_node].append((adj_cost, adj_node))
        idx += 2

def dfs(x, dist):
    for next in graph[x]:
        next_dist, next_node = next
        if -1 == visited[next_node]:
            update_dist = dist + next_dist
            visited[next_node] = update_dist
            dfs(next_node, update_dist)

visited = [-1] * (V+1)
visited[1] = 0
dfs(1, 0)

faraway_value1 = 0
faraway_index1 = 1
for i in range(len(visited)):
    if faraway_value1 < visited[i] and visited[i] != -1:
        faraway_value1 = visited[i]
        faraway_index1 = i

visited = [-1] * (V+1)
visited[faraway_index1] = 0
dfs(faraway_index1, 0)

faraway_value2 = 0
faraway_index2 = 1

for i in range(len(visited)):
    if faraway_value2 < visited[i] and visited[i] != -1:
        faraway_value2 = visited[i]
        faraway_index2 = i
print(faraway_value2)