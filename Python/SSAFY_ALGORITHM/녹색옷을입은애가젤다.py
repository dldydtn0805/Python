import sys
sys.stdin = open('input.txt')

tc = 1
while True:
    n = int(input())
    if not n:
        break
    lupy = [list(map(int, input().split())) for _ in range(n)]
    queue = []
    # Min 함수 구현하는것처럼 visited 선언
    visited = [[1e9]*n for _ in range(n)]
    queue.append((0, 0))
    visited[0][0] = lupy[0][0]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    # BFS로 풀어보자
    while queue:
        i, j = queue.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<n and 0<=nj<n:
                # # 만약 갱신할 루피가 더 작을때만 방문한다
                if visited[ni][nj] > visited[i][j] + lupy[ni][nj]:
                    visited[ni][nj] = visited[i][j] + lupy[ni][nj]
                    queue.append((ni, nj))

    print(f'Problem {tc}:', visited[n-1][n-1])
    tc += 1