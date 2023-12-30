import sys
# sys.stdin = open('input.txt')
import heapq
input = sys.stdin.readline
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for e in range(E):
    node1, node2, dist = map(int, input().split())
    graph[node1].append((dist, node2))
    graph[node2].append((dist, node1))

v1, v2 = map(int, input().split())

# 전형적인 다익스트라
def dijkstra(start):
    distance = [1e9] * (N+1)
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        current_dist, current_node = heapq.heappop(heap)
        if current_dist > distance[current_node]:
            continue
        for update in graph[current_node]:
            update_dist, update_node = update
            calculated_dist = update_dist + distance[current_node]
            if calculated_dist < distance[update_node]:
                distance[update_node] = calculated_dist
                heapq.heappush(heap, (calculated_dist, update_node))
    return distance

D_1 = dijkstra(1)
D_V1 = dijkstra(v1)
D_V2 = dijkstra(v2)
# 1 -> v1 -> v2 -> N 경로
ans1 = 0

ans1 += D_1[v1]
ans1 += D_V1[v2]
ans1 += D_V2[N]

# 1 -> v2 -> v1 -> N 경로
ans2 = 0
ans2 += D_1[v2]
ans2 += D_V2[v1]
ans2 += D_V1[N]

# 두 경로중 더 짧은 경로를 출력한다
ans = min(ans1, ans2)

if ans >= 1e9:
    print(-1)
else:
    print(ans)