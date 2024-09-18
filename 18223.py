import sys, heapq
input = sys.stdin.readline
def dijkstra(si):
    heap = []
    distance = [1e9 for _ in range(V+1)]
    heapq.heappush(heap, (0, si))
    distance[si] = 0
    while heap:
        cw, ci = heapq.heappop(heap)
        if cw > distance[ci]:
            continue
        for nw, ni in adj_list[ci]:
            new_dist = nw + distance[ci]
            if new_dist < distance[ni]:
                distance[ni] = new_dist
                heapq.heappush(heap, (new_dist, ni))
    return distance
V, E, P = map(int, input().split())
adj_list = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    adj_list[a].append((c, b))
    adj_list[b].append((c, a))
A = dijkstra(1)
B = dijkstra(P)
if A[V] >= A[P] + B[V]:
    print('SAVE HIM')
else:
    print('GOOD BYE')
