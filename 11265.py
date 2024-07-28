import sys
input = sys.stdin.readline
import heapq
from collections import defaultdict
def dijkstra(A):
    heap = []
    heapq.heappush(heap, (0, A))
    distance = [1e9 for _ in range(N)]
    distance[A] = 0
    while heap:
        cur_w, cur_i = heapq.heappop(heap)
        if cur_w > distance[cur_i]:
            continue
        for next_i in range(len(adjacent_list[cur_i])):
            next_w = adjacent_list[cur_i][next_i]
            next_distance = distance[cur_i] + next_w
            if next_distance < distance[next_i]:
                distance[next_i] = next_distance
                heapq.heappush(heap, (next_distance, next_i))
                distance[next_i] = next_distance
    return distance

N, M = map(int, input().split())
adjacent_list = [list(map(int, input().split())) for _ in range(N)]
dic = defaultdict(list)
for i in range(N):
    dic[i] = dijkstra(i)
for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    if dic[A][B] <= C:
        print('Enjoy other party')
    else:
        print('Stay here')

