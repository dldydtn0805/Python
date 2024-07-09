import sys
# sys. stdin = open('input.txt')
import heapq
input = sys.stdin.readline
def djk(node):
    heap = []
    # 힙에 비용, 노드, 루트 순으로 기록한다
    heapq.heappush(heap, (0, node, str(node)))
    total_route[node] = str(node)
    visited[node] = 0
    while heap:
        cur_w, cur_s, cur_r = heapq.heappop(heap)
        # 현재 가중치가 현재 기록된 비용보다 높은경우에 볼것도없다
        if cur_w > visited[cur_s]:
            continue
        # 그래프에서 다음 가중치와 위치를 가져옵니다
        for next in graph[cur_s]:
            next_w, next_s = next
            # 현재 가중치와 다음 가중치를 더한 값이 기록된 다음 비용보다 작을 때만 갱신
            if cur_w + next_w < visited[next_s]:
                visited[next_s] = cur_w + next_w
                # 다음 루트를 작성해주는데 사이에 공백을 넣어서 구분이 가게 문자열에 기록되도록한다
                # 그 이유는 두자리 수 이상일 경우 이렇게 해야만 출력이 제대로 나옵니다
                next_r = cur_r + ' ' +str(next_s)
                total_route[next_s] = next_r
                # 힙에 비용, 노드, 루트 순으로 기록한다
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
# 루트의 길이 보다 1 적게 공백이 있을 것이기 때문에 이렇게 계산했다
print(total_route[e].count(' ')+1)
print(total_route[e])
