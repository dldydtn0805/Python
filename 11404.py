import sys
input = sys.stdin.readline
import heapq

def dijkstra(start_node):
    heap = []
    distanse = [1e9 for _ in range(n)]
    heapq.heappush(heap, (0, start_node))
    distanse[start_node] = 0
    while heap:
        current_weight, current_node = heapq.heappop(heap)
        if current_weight > distanse[current_node]:
            continue
        for next_weight, next_node in adjacent_list[current_node]:
            next_distance = next_weight + distanse[current_node]
            if distanse[next_node] > next_distance:
                distanse[next_node] = next_distance
                heapq.heappush(heap, (next_distance, next_node))
    return distanse

n = int(input())
m = int(input())
adjacent_list = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    a -= 1
    b -= 1
    adjacent_list[a].append([c, b])

for i in range(n):
    res = dijkstra(i)
    for j in range(len(res)):
        if res[j] != 1e9:
            print(res[j], end=' ')
        else:
            print(0, end=' ')
    print()
