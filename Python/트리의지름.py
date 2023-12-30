import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq
N  = int(input())
graph = [[] for _ in range(N+1)]
for n in range(N-1):
    node1, node2, dist = map(int, input().split())
    graph[node1].append((dist, node2))
    graph[node2].append((dist, node1))

# 다익스트라 기본 형태
def djikstra(node):
    heap = []
    distance = [1e9]*(N+1)
    heapq.heappush(heap, (0, node))
    distance[node] = 0
    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        if cur_dist > distance[cur_node]:
            continue
        for next in graph[cur_node]:
            next_dist, next_node = next
            update_dist = distance[cur_node] + next_dist
            if update_dist < distance[next_node]:
                distance[next_node] = update_dist
                heapq.heappush(heap, (update_dist, next_node))

    # 거리값을 return
    return distance

# 루트노드인 1에서 각 노드까지의 거리를 찾는다
ans1 = djikstra(1)
max_v1 = 0
max_v1_idx = 1
# 우선 루트노드에서 가장 먼 노드의 위치를 찾는다
for i in range(len(ans1)):
    if max_v1 < ans1[i] and ans1[i] != 1e9:
        max_v1 = ans1[i]
        max_v1_idx = i

# 1차로 찾은 노드에서 또다시 각 노드까지의 거리를 찾는다
ans2 = djikstra(max_v1_idx)
max_v2 = 0
for i in range(len(ans2)):
    if max_v2 < ans2[i] and ans2[i] != 1e9:
        max_v2 = ans2[i]
# 가장 먼곳에 까지의 최단거리를 출력하면 트리의 지름이 된다
print(max_v2)