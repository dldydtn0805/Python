import sys, heapq
sys.stdin = open('input.txt')

def djk(start):
    heap = []
    heapq.heappush(heap, (0, start))
    visited[start] = 0
    while heap:
        w, cur = heapq.heappop(heap)
        for next in graph[cur]:
            next_v = w + next[0]
            next_i = next[1]
            if visited[next_i] > next_v:
                visited[next_i] = next_v
                heapq.heappush(heap, ((next_v, next_i)))
        if cur < d:
            cur += 1
            if visited[cur] > w + 1:
                w += 1
                visited[cur] = w
                heapq.heappush(heap, ((w, cur)))

n, d = map(int, input().split())
graph = [[] for _ in range(d+1)]
visited = [1e9]*(d+1)
start_point = []
for _ in range(n):
    f, t, w = map(int, input().split())
    if t > d:
        continue
    graph[f].append((w, t))
    start_point.append(f)
min_v = 1e9
djk(0)
print(visited[-1])


