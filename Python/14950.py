import heapq
import sys
input = sys.stdin.readline

def prim(start, t):
    visited = [False for _ in range(N)]
    heap = []
    visited[start] = True
    총거리 = 0
    공포 = 0
    heapq.heappush(heap, (0, start))
    while heap:
        현재가중치, 현재노드 = heapq.heappop(heap)
        if not visited[현재노드]:
            visited[현재노드] = True
            총거리 += (현재가중치 + 공포 * t)
            공포 += 1
        for 다음가중치, 다음노드 in graph[현재노드]:
            if not visited[다음노드]:
                heapq.heappush(heap, (다음가중치, 다음노드))
    return 총거리

N, M, t = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    graph[A].append((C,B))
    graph[B].append((C,A))

print(prim(0, t))
