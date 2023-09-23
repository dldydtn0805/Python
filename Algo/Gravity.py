"""
상자들이 쌓여잇는 방이 있다

방이 오른쪽으로 90도 회전하여 상자들이 중력의 영향을 받아 낙하할때

낙차가 가장 큰 상자를 구하여 낙차를 리턴하는 프로그램을 작성하라

중력은 회전이 완료된 후 적용

상자들은 모두 한쪽 벽면에 붙여진상태로 쌓여 2차원의 형태

벽에서 떨어져서 쌓인 상자는 없다

방의 가로는 항상 100 세로도 100

상자는 최소 0 최대 100 높이로 쌓을 수 있다

입력

첫줄에는 방의 가로 길이가 주어지고

다음 줄에는 쌓여있는 상자의 수가 주어진다

# 각 상자의 낙차는, 방의 가로 길이 - 각 인덱스 - (각 인덱스보다 큰 개수)
"""


import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 최대 낙차
    max_fallen = 0
    # 각 인덱스의 상자의 번호 순회
    for i in range(N):
        cnt = 0
        # 각 인덱스 상자부터 맨 끝 상자까지 순회
        for j in range(i+1, N-1):
            #j번째 상자가 i번째 상자보다 크다면,
            if arr[j] >= arr[i]:
                #카운트를 1 늘려준다
                cnt += 1
        # 낙차 계산 ( 총 길이 - 인덱스 - 더 큰 상자 개수 )
        fallen = N - (i+1) - cnt
        # 최대 낙차 갱신
        if max_fallen < fallen:
            max_fallen = fallen
    print(f'#{tc}', max_fallen)



