import sys
sys.stdin = open('input.txt')

def bfs(i, j, color):
    visited[i][j] = color
    queue = []
    di = [-1, -1, -1, 0, 1, 1, 1, 0]
    dj = [0, 1, -1, 1, 1, 0, -1, -1]

    #8개 방향에 실행
    for k in range(8):
        # 맨 끝까지 판단
        for p in range(1, n + 1):
            ni = i + di[k] * p
            nj = j + dj[k] * p
            if 0 <= ni < n and 0 <= nj < n:
                # 방문한적 없다면
                if visited[ni][nj] == 0:
                    break
                # 돌이 놓여져 있다면
                else:
                    #돌 색 같다면
                    if visited[ni][nj] == color:
                        while queue:
                            x, y = queue.pop()
                            visited[x][y] = color
                            # print(visited)
                    # 돌 색 다르다면
                    elif visited[ni][nj] != color:
                        queue.append((ni, nj))
        # 잔여 큐
        queue.clear()

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    visited = [[0] * (n) for _ in range(n)]
    half = n//2
    visited[half - 1][half] = 2
    visited[half][half- 1] = 2
    visited[half - 1][half- 1] = 1
    visited[half][half] = 1
    for _ in range(m):
        i, j, color = map(int, input().split())
        # print('place' ,i, j)
        # print(visited)
        bfs(i - 1, j - 1, color)
        # print(visited)
    a = 0
    b = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 2:
                a += 1
            if visited[i][j] == 1:
                b += 1
    print(f'#{tc}', b, a)