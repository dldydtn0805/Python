import sys
sys.stdin = open('input.txt')

def dfs():
    cnt = 0
    # 방문 처리
    visited = [[0]*(M) for _ in range(N)]
    stack = []
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for i in range(N):
        for j in range(M):
            # 만약 배추가 심어져있고 방문 안했을때
            if baechu[i][j] == 1 and visited[i][j] == 0 :
                # 벌레 카운트 방문처리
                cnt += 1
                visited[i][j] = 1
                # 내가 자꾸 제출 틀린 이유 = 자기 자신을 스택에 안넣음
                stack.append((i, j))
                while True:
                    for k in range(4):
                        ni = i + di[k]
                        nj = j + dj[k]
                        # 상하좌우 네방향에 배추가 심어져 있는데 방문 안했을때
                        if 0<=ni<N and 0<=nj<M:
                            if baechu[ni][nj] == 1 and visited[ni][nj] == 0:
                                visited[ni][nj] = 1
                                stack.append((ni, nj))
                        # 인접한 배추로 이동
                    if len(stack)>0:
                        i, j = stack.pop()

                        # 다 전염 시켰으면 다음 배추로 넘어가기
                    else:
                        break

    return cnt




T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    baechu = [[0]*(M) for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        baechu[y][x] = 1
    print(dfs())