"""
n명의 손님

m초의 시간동안 k개의 붕어빵

지연 없음

if 모든 손님에게 기다리는 시간 없이 붕어빵 제공 가능하면
    possible
else:
    impossible

"""


import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    # n = 사람,  m = 시간, k = 붕어빵
    n, m, k = map(int, input().split())
    waiting = list(map(int, input().split()))
    # 붕어
    queue = []
    flag = True
    cnt = 1
    # 웨이팅이 존재하는동안 반복
    while waiting:
        # 만약 굽기 전에 도착한 사람이 있다면 ?
        for i in waiting:
            # 만약 먼저온 사람이 있으면 ?
            if i < m*cnt:
            # 붕어빵이 있다면 Fail
                if not queue:
                    flag = False
            # 붕어빵이 있다면 배급
                else:
                    # 웨이팅 제거, 붕어빵 1개 out
                    waiting.remove(i)
                    queue.pop()
        # 붕어빵 k개 채워넣기
        for _ in range(k):
            queue.append(1)
        # 구워지고 난 다음 온 사람들
        for i in waiting:
            if m*cnt <= i < m*(cnt+1):
                # 붕어빵이 없다면 사고임
                if not queue:
                    flag = False
                # 붕어빵이 있다면 배급
                else:
                    waiting.remove(i)
                    queue.pop()
        # 다음번 붕어빵으로 넘어가기
        cnt += 1
    if flag:
        print(f'#{tc}', 'Possible')
    else:
        print(f'#{tc}', 'Impossible')

