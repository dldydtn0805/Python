import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    # 단방향 그래프 입력
    graph[u].append((w, v))

def djikstra(start):
    distance = [1e9]*(V+1)
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        # 기록된 현재 노드까지의 거리보다 현재 거리가 더 길면 의미가 없으므로 continue
        if cur_dist > distance[cur_node]:
            continue
        for next in graph[cur_node]:
            next_dist, next_node = next
            # 업데이트할 거리 = 다음 노드까지의 거리 + 기록된 현재 노드까지의 거리
            update_dist = next_dist + distance[cur_node]
            # 업데이트할 거리가 기록된 다음 노드까지의 거리보다 작을때만 갱신해준다
            if update_dist < distance[next_node]:
                distance[next_node] = update_dist
                heapq.heappush(heap, (update_dist, next_node))

    return distance
ans = djikstra(K)

for i in range(1, len(ans)):
    if ans[i] == 1e9:
        print('INF')
    elif i == K:
        print(0)
    else:
        (print(ans[i]))