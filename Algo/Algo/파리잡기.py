import sys
sys.stdin = open('input.txt')

def max_v(x,y):
    if x > y:
        return x
    elif x < y:
        return y
    elif x == y:
        return x

T = int(input())
for tc in range(1, T+1):
    #N 크기의 전체 파리, M 크기의 파리채
    N, M = map(int, input().split())
    #전체 파리의 배열
    arr = [list(map(int, input().split())) for _ in range(N)]

    #기본 파리채 설정
    di = [0, 1, 1]
    dj = [1, 1, 0]
    max_total = 0
    #파리 맵 순회
    for i in range(N):
        for j in range(N):
            # 한번에 잡을 수 있는 총 파리 개수를 total 로 선언하고,
            # 기준 인덱스의 파리 개수를 total 에 할당
            total = arr[i][j]
            # 기준 인덱스에서 파리채 모양으로 탐색
            # 반복문 안에서 파리채 크기 M 만큼 곱해주면서 파리채 모양을 만든다
            for k in range(3):
                for p in range(1, M):
                    ni = i+di[k]*p
                    nj = j+di[k]*p
                    # total 에 해당 인덱스 더한다
                    if 0 <= ni < N and 0 <= nj < N:
                        total += arr[ni][nj]
                    # 한번에 잡을 수 있는 총 파리의 개수의 최대값을 구한다


            max_total = max_v(total, max_total)
    print(f'{tc}', max_total)