# import sys
# sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # 단어 퍼즐의 변의 길이 N, 단어의 길이 K
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 단어 들어갈 수 있는 횟수
    result = 0
    cnt = 0
    # 가로 방향으로 퍼즐 탐색하기
    for i in range(N):
        for j in range(N):
            # 만약, 해당 항목이 하얀색이라면, 카운팅에 1을 한다
            if arr[i][j] == 1:
                cnt += 1
            # 만약, 현재 항목이 검정색이라면, 카운팅은 0으로 초기화 한다
            if arr[i][j] == 0:
                cnt = 0
            # 만약, 현재 항목 우측이 검정색인 동시에, 카운팅이 K까지 세졌다면
            if 0 <= j+1 < N: # 범위를 정상으로 제한하기
                if cnt == K and arr[i][j+1] ==0:
                    # 최종 카운트에 1을 더해준다
                    result += 1
                    # 다시 카운팅은 0으로 초기화 한다
                    cnt = 0
            # 만약, 현재 위치가 마지막 항목인 동시에, 카운팅이 K까지 세졌다면
            if cnt == K and j == N-1:
                # 최종 카운트에 1을 더해준다
                result += 1
                # 다시 카운팅은 0으로 초기화한다
                cnt = 0
            # 만약, 현재 위치가 행의 마지막 항목이기만 하다면,
            elif j == N-1:
                #  다시 카운팅은 0으로 초기화한다
                cnt = 0

    # 세로 방향으로 퍼즐 탐색하기
    for i in range(N):
        for j in range(N):
            # 만약, 현재 항목이 하얀색이라면, 카운팅에 1을 한다
            if arr[j][i] == 1:
                cnt += 1
            # 만약, 현재 항목이 검정색이라면, 카운팅을 0으로 초기화한다
            if arr[j][i] == 0:
                cnt = 0
            # 만약, 카운팅이 K까지 세졌고, 현재 항목의 아래쪽이 0이라면 (세로 탐색의 아래 항목, a[j+1][i])
            if 0 <= j+1 < N: # 범위가 정상적일 때
                if cnt == K and arr[j+1][i] == 0:
                    #최종 카운팅에 1을 더하고, 카운팅을 리셋한다
                    result += 1
                    cnt = 0
            # 만약, 카운팅이 K까지 세졌고, 현재 위치가 열의 마지막 항목이라면,
            if cnt == K and j == N - 1:
                #최종 카운팅에 1을 더하고, 카운팅을 리셋한다
                result += 1
                cnt = 0
            # 만약 현재 위치가 열의 마지막 항목이라면,
            elif j == N - 1:
                # 카운팅 리셋
                cnt = 0
    print(f'#{tc}', result)




