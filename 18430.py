def backtracking(i, j, value):
    if j == M:
        backtracking(i+1, 0, value)
    elif i == N:
        global ans
        ans = max(ans, value)
        return
    else:
        if visited[i][j]:
            if j < M:
                backtracking(i, j+1, value)
            elif i < N:
                backtracking(i+1, 0, value)
        else:
            for direction in directions:
                flag_cnt = 0
                for di, dj in direction:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M:
                        if not visited[ni][nj]:
                            flag_cnt += 1
                if flag_cnt == 3:
                    next_value = value
                    for di, dj in direction:
                        ni, nj = i + di, j + dj
                        visited[ni][nj] = 1
                        if di == 0 and dj == 0:
                            next_value += 2 * arr[ni][nj]
                        else:
                            next_value += arr[ni][nj]
                    if j < M:
                        backtracking(i, j+1, next_value)
                    elif i < N:
                        backtracking(i+1, 0, next_value)
                    for di, dj in direction:
                        ni, nj = i + di, j + dj
                        visited[ni][nj] = 0
            if j < M:
                backtracking(i, j + 1, value)
            elif i < N:
                backtracking(i + 1, 0, value)

N, M = map(int, input().split())

directions = [
    [[0,0],[1,0],[0,-1]],
    [[0,0],[-1,0],[0,-1]],
    [[0,0],[0,1],[-1,0]],
    [[0,0],[0,1],[1,0]]
]

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
ans = 0
if N < 2 or M < 2:
    print(0)
else:
    backtracking(0, 0, 0)
    print(ans)
