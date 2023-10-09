import sys
# sys. stdin = open('input.txt')
import heapq
input = sys.stdin.readline
def djk(node):
    heap = []
    heapq.heappush(heap, (0, node, str(node)))
    total_route[node] = str(node)
    visited[node] = 0
    while heap:
        cur_w, cur_s, cur_r = heapq.heappop(heap)
        if cur_w > visited[cur_s]:
            continue
        for next in graph[cur_s]:
            next_w, next_s = next
            if cur_w + next_w < visited[next_s]:
                visited[next_s] = cur_w + next_w
                next_r = cur_r + ' ' +str(next_s)
                total_route[next_s] = next_r
                heapq.heappush(heap, (visited[next_s], next_s, next_r))

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y, w = map(int, input().split())
    graph[x].append((w, y))
s, e = map(int, input().split())
visited = [1e9 for _ in range(N+1)]
total_route = [[] for _ in range(N+1)]
djk(s)
print(visited[e])
print(total_route[e].count(' ')+1)
print(total_route[e])
