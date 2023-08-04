# import sys
# sys.stdin = open('input.txt')

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
    #최대 총합
    max_total = 0
    #N번 반복
    #전체 정사각형의 가로 범위 설정
    for i in range(N):
        #전체 정사각형의 세로 범위 설정
        for j in range(N):
            # 총합
            total = 0
            #변의 길이 M인 정사각형을 구성
            # M 크기의 파리채의 가로 좌표
            for ni in range(i, i+M):
                # M 크기의 파리채의 세로 좌표
                for nj in range(j, j+M):
                    if 0 <= ni < N and 0 <= nj < N:
                        # 한번에 때려 잡는 파리의 수
                        total += arr[ni][nj]
            # 한번에 때려잡는 파리의 수의 최대값
            max_total = max_v(total, max_total)
    print(f'#{tc}', max_total)
