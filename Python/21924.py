import sys
input = sys.stdin.readline
import heapq

def prim(si):
    visited = [0 for _ in range(N)]
    visited[si] = 1
    candidate = adj_list[si]
    heapq.heapify(candidate)
    mst = []
    distance = 0
    while candidate:
        cur_w, cur_i, next_i = heapq.heappop(candidate)
        if visited[next_i] == 0:
            visited[next_i] = 1
            mst.append((cur_i, next_i))
            distance += cur_w
            for node in adj_list[next_i]:
                if not visited[node[2]]:
                    heapq.heappush(candidate, node)
    for check in visited:
        if not check:
            return -1
    return total_cost - distance

N, M = map(int, input().split())
adj_list = [[] for _ in range(N)]
total_cost = 0
for _ in range(M):
    a, b, cost = map(int, input().split())
    a -= 1
    b -= 1
    total_cost += cost
    adj_list[a].append((cost, a, b))
    adj_list[b].append((cost, b, a))
print(prim(0))
