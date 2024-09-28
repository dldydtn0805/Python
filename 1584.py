import sys, heapq
input = sys.stdin.readline

def dijkstra(si,sj):
    heap = []
    distance = [[1e9 for _ in range(K)] for _ in range(K)]
    heapq.heappush(heap, (0, si, sj))
    distance[si][sj] = 0
    while heap:
        cw, ci, cj = heapq.heappop(heap)
        if cw > distance[ci][cj]:
            continue
        for di, dj in [[-1,0],[0,1],[1,0],[0,-1]]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < K and 0 <= nj < K:
                if weights[ni][nj] != -1:
                    if distance[ni][nj] > distance[ci][cj] + 1:
                        next_distance = distance[ci][cj] + weights[ni][nj]
                        heapq.heappush(heap, (next_distance, ni, nj))
                        distance[ni][nj] = next_distance
    return distance

K = 501

weights = [[0 for _ in range(K)] for _ in range(K)]
N = int(input())
for _ in range(N):
    X1, Y1, X2, Y2 = map(int, input().split())
    for i in range(min(X1, X2), max(X1, X2)+1):
        for j in range(min(Y1, Y2), max(Y1, Y2)+1):
            weights[i][j] = 1
M = int(input())
for _ in range(M):
    X1, Y1, X2, Y2 = map(int, input().split())
    for i in range(min(X1, X2), max(X1, X2)+1):
        for j in range(min(Y1, Y2), max(Y1, Y2)+1):
            weights[i][j] = -1
weights[0][0] = 0
dist = dijkstra(0, 0)
if dist[-1][-1] == 1e9:
    print(-1)
else:
    print(dist[-1][-1])
