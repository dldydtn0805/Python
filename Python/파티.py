import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

N, M, X = map(int, input().split())

graph = [[] for _ in range(N)]

# 다익스트라 그래프 생성
for _ in range(M):
    start, end, dist = list(map(int, input().split()))
    graph[start-1].append((dist, end-1))


# 다익스트라 기본 형태
def dijkstra(node):
    heap = []
    distance = [1e9]*N
    heapq.heappush(heap, (0, node))
    distance[node] = 0
    while heap:
        current_dist, current_node = heapq.heappop(heap)
        if current_dist > distance[current_node]:
            continue
        for now in graph[current_node]:
            now_dist, now_node = now
            calculated_dist = now_dist + current_dist
            if calculated_dist < distance[now_node]:
                distance[now_node] = calculated_dist
                heapq.heappush(heap, (calculated_dist, now_node))
    return distance

# 왕복으로 갔다와야하므로 각 마을별 파티 왕복 거리 저장
ans = [0 for _ in range(N)]

for i in range(N):
    # 파티에서 마을로 갈때 거리 저장
    if i == X-1:
        temp = dijkstra(i)
        for j in range(len(temp)):
            ans[j] += temp[j]
    # 마을에서 파티로 갈때 거리 저장
    else:
        temp = dijkstra(i)
        ans[i] += temp[X-1]

# 가장 먼 마을 출력
print(max(ans))

