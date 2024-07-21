import sys
input = sys.stdin.readline
import heapq
import math

def walk(si, sj, ei, ej):
    return math.sqrt((si - ei)**2 + (sj - ej)**2)

def djikstra():
    distance = [1e9 for _ in range(N+2)]
    distance[0] = 0
    heap = [[0, 0]]
    while heap:
        time, next = heapq.heappop(heap)
        if time > distance[next] :
            continue
        for i in range(len(adj_list)):
            if next != i:
                if distance[i] > time + adj_list[i][next]:
                    distance[i] = time + adj_list[i][next]
                    heapq.heappush(heap, [distance[i], i])
    return distance

sj, si = map(float, input().split())
ej, ei = map(float, input().split())
N = int(input())
canons = []
for _ in range(N):
    cj, ci = map(float, input().split())
    canons.append([ci, cj])

arr = [[si, sj]] + canons + [[ei, ej]]
adj_list = [[0]*(N+2) for _ in range(N+2)]

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if i == 0:
            adj_list[i][j] = walk(arr[i][0],arr[i][1],arr[j][0],arr[j][1])/5
        else:
            distance = walk(arr[i][0],arr[i][1],arr[j][0],arr[j][1])
            adj_list[i][j] = walk(arr[i][0],arr[i][1],arr[j][0],arr[j][1])/5
            if distance > 50.0:
                adj_list[i][j] = min(adj_list[i][j], 2+(distance-50)/5)
            elif distance == 50.0:
                adj_list[i][j] = 2.0
            else:
                adj_list[i][j] = min(adj_list[i][j], 2+(50-distance)/5)
        adj_list[j][i] = adj_list[i][j]

print(f'{djikstra()[N+1]:6f}')
