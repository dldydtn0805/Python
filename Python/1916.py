import sys
input = sys.stdin.readline
import heapq

def dijkstra(node):
    heap = []
    heapq.heappush(heap, (0, node))
    distance = [1e9 for _ in range(N)]
    distance[node] = 0
    while heap:
        current_distance, current_node = heapq.heappop(heap)
        if current_distance > distance[current_node]:
            continue
        for next_weight, next_node in adjacent_list[current_node]:
            next_distance = distance[current_node] + next_weight
            if next_distance < distance[next_node]:
                distance[next_node] = next_distance
                heapq.heappush(heap, (next_distance, next_node))
    return distance

N = int(input())
M = int(input())
adjacent_list = [[] for _ in range(N)]
for _ in range(M):
    start, end, distance = map(int, input().split())
    start -= 1
    end -= 1
    adjacent_list[start].append((distance, end))

start_node, end_node = map(int,input().split())
start_node -= 1
end_node -= 1
res = dijkstra(start_node)
print(res[end_node])
