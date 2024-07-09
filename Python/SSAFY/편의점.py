import sys, heapq
# sys.stdin = open('input.txt')
input = sys.stdin.readline
def bfs(start):
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        cur_w, cur = heapq.heappop(heap)
        if visited[cur] < cur_w:
            continue
        if cur in home:
            heapq.heappush(result, (cur_w, cur))
            return
        for to in range(len(graph[cur])):
            next = graph[cur][to]
            next_v = next[0] + cur_w
            next_i = next[1]
            if visited[next_i] <= next_v:
                continue
            heapq.heappush(heap, (next_v, next_i))
            visited[next_i] = next_v


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    f, t, w = map(int, input().split())
    graph[f].append((w,t))
    graph[t].append((w,f))
p, q = map(int, input().split())
home = list(map(int, input().split()))
mart = list(map(int, input().split()))
home.sort()
mart.sort()
result = []
for i in mart:
    visited = [int(1e9)]*(n+1)
    bfs(i)
print(sorted(result)[0][1])