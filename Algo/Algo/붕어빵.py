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
    queue = []
    flag = True
    # 시간 다 지났을때
    cnt = 1
    while waiting:
        # 붕어빵 k개 까지 채워넣기
        for _ in range(k):
            queue.append(1)
        for i in waiting:
            # 만약 먼저온 사람이 있으면 flag = False
            if i < m*cnt:
                waiting.remove(i)
                flag = False
            # 만들어 진 후에 도착하고 붕어빵 있다면
            elif m*cnt <= i and queue:
                waiting.remove(i)
                queue.pop()
        cnt += 1
    print(tc, flag)

