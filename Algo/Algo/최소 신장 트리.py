import sys, heapq
# sys.stdin = open('input.txt')
def prim(start):
    heap = []
    heapq.heappush(heap, (0, start))
    sum_v = 0
    while heap:
        pv, pi = heapq.heappop(heap)
        if visited[pi]:# debug
            continue
        sum_v += pv
        visited[pi] = 1 # debug
        for next in graph[pi]:
            nv = next[0]
            ni = next[1]
            if visited[ni]:
                continue
            heapq.heappush(heap, (nv, ni))
    return sum_v
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph[n1].append((w, n2))
        graph[n2].append((w, n1))
    visited = [0]*(V+1)
    print(f'#{tc}', prim(2))
