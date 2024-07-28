import sys
input = sys.stdin.readline
import heapq

def dijkstra(start_node):
    heap = []
    heapq.heappush(heap, [0, start_node])
    distance = [1e9 for _ in range(100001)]
    distance[start_node] = 0
    while heap:
        current_distance, current_node = heapq.heappop(heap)
        if current_distance > distance[current_node]:
            continue
        for next_weight, next_node in [[1, current_node+1], [1, current_node-1], [0, current_node*2]]:
            if 0 <= next_node < 100001:
                next_distance = next_weight + distance[current_node]
                if next_distance < distance[next_node]:
                    distance[next_node] = next_distance
                    heapq.heappush(heap, (next_distance, next_node))
    return distance
n, k = map(int, input().split())

print(dijkstra(n)[k])
