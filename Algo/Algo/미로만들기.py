import sys, heapq
# sys.stdin = open('input.txt')

def djk():
    heap = []
    heapq.heappush(heap, (0, 0, 0))
    visited[0][0] = 0
    while heap:
        next = heapq.heappop(heap)
        w, i, j = next[0], next[1], next[2]
        if i == n-1 and j == n-1:
            return w
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            ni, nj = i + di, j + dj
            if 0<= ni < n and 0<= nj< n:
                if graph[ni][nj] == 1:
                    if visited[ni][nj] > w:
                        heapq.heappush(heap, (w, ni, nj))
                        visited[ni][nj] = w
                elif graph[ni][nj] == 0:
                    if visited[ni][nj] > w+1:
                        visited[ni][nj] = w + 1
                        heapq.heappush(heap, (w+1, ni, nj))

    pass
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[1e9]*n for _ in range(n)]
print(djk())