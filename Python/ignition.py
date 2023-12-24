import sys, heapq
sys.stdin = open('input.txt')

def djk(start):
    heap = []
    heapq.heappush(heap, (0, start))
    visited[start] = 0
    while heap:
        w, cur = heapq.heappop(heap)
        for next in graph[cur]:
            next_v = next[0] + w
            next_i = next[1]
            if visited[next_i] > next_v:
                visited[next_i] = next_v
                heapq.heappush(heap, (next_v, next_i))

    pass
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
start_point = []
for _ in range(M):
    S, E, L = map(int, input().split())
    graph[S].append((L, E))
    graph[E].append((L, S))
    start_point.append(S)
max_v = 0
min_v = 1e9
result = []
for i in range(N+1):
    visited = [1e9]*(N+1)
    djk(i)
    max_v = 0
    for k in range(len(graph)):
        for j in range(len(graph[k])):
            temp = 0
            # 왼쪽 노드 불붙는 시간
            x = (graph[k][j])
            left = visited[k]
            # 오른쪽 노드 불붙는 시간
            right = visited[x[1]]
            cur = x[0]
            if left == 1e9 or right == 1e9:
                continue
            if left > right:
                temp = left + (cur - (left-right)) / 2
            elif right > left:
                temp = right + (cur - (left+right)) / 2
            elif left == right:
                temp = left + cur / 2
            max_v = max(max_v, temp)
    if max_v == 0:
        continue
    min_v = min(max_v, min_v)
print(min_v)
