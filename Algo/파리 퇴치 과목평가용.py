"""
NxN 배열 안의 숫자는 해당 영역에 존재하는 파리의 갯수를 의미한다

아래는 N=5의 예이다

MxM 크기의 파리채를 한번 내리쳐 최대한 많은 파리를 죽이고자 한다

죽은 파리의 갯수는?

입력

N*M이 주어지고

N줄에 걸쳐 N*N 배열이 주어진다
"""

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 최대로 잡을 수 있는 파리 개수
    max_cnt = 0
    # N 크기의 파리 떼
    for i in range(N):
        for j in range(N):
            # 잡을 수 있는 파리 개수
            sum_cnt = 0
            # M 크기의 파리채 구성
            for k in range(i, i+M):
                for p in range(j, j+M):
                    if 0<=k<N and 0<=p<N:
                        sum_cnt += arr[k][p]
            # 최대로 잡을 수 있는 파리 개수 갱신
            if max_cnt < sum_cnt:
                max_cnt = sum_cnt

    print(f'#{tc}', max_cnt)