import heapq

# sys.stdin = open('input.txt')
T = int(input())


def djk(si, sj, value):
    heap = []
    heapq.heappush(heap, (value, si, sj))
    visited[si][sj] = 0
    while heap:
        precost, prei, prej = heapq.heappop(heap)
        if precost > visited[prei][prej]:
            continue
        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ni, nj = prei + di, prej + dj
            if 0 <= ni < n and 0 <= nj < n:

                ncost = precost + 1
                if arr[ni][nj] > arr[prei][prej]:
                    ncost += (arr[ni][nj] - arr[prei][prej])
                if visited[ni][nj] <= ncost:
                    continue
                heapq.heappush(heap, (ncost, ni, nj))
                visited[ni][nj] = ncost


for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[1e9] * n for _ in range(n)]
    djk(0, 0, 0)
    # print(visited)
    print(f'#{tc}', visited[n - 1][n - 1])