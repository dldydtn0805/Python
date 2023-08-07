"""
ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.

회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.

"""

# import sys
# sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    # 가로 탐색
    for i in range(N):
        check = 1
        # 회문
        word = ''
        for j in range(N):
            # 조사 범위 설정 (길이가 N이고 회문의 길이가 M일때)
            if 0<= N-M+j<N and 0<= N-1-j < N:
                # 만약 회문이라면, 회문을 작성한다
                if arr[i][N-M+j] == arr[i][N-1-j]:
                    word += arr[i][N-M+j]
                # 만약 회문이 아니라면, check가 0이 된다
                if arr[i][N-M+j] != arr[i][N-1-j]:
                    check = 0
        # 회문이 다 작성되었고, 출력한다
        if check == 1:
            print(f'#{tc}', word)

    # 세로 탐색
    for i in range(N):
        # 회문이면 1을 반환, 아니면 0을 반환
        check = 1
        # 회문
        word = ''
        for j in range(N):
            # 조사 범위 설정 (길이가 N이고 회문의 길이가 M일때)
            if 0<= N-M+j < N and 0 <= N-1-j < N:
                # 만약 회문이라면, 회문을 작성한다
                if arr[N-M+j][i] == arr[N - 1 - j][i]:
                    word += arr[N-M+j][i]
                # 만약 회문이 아니라면, check가 0이 된다
                if arr[N-M+j][i] != arr[N - 1 - j][i]:
                    check = 0
        #회문이 다 작성되었으면 출력한다
        if check == 1:
            print(f'#{tc}', word)