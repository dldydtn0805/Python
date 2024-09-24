import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    houses = list(map(int, input().split()))
    houses = [(houses[i], i) for i in range(N)]
    houses = deque(houses)
    queue = deque((list(houses)[:M]))

    money = 0
    for i in range(M):
        money += queue[i][0]

    ans = 0
    for i in range(N):
        if money < K:
            ans += 1
        money -= queue.pop()[0]
        houses.rotate(1)
        money += houses[0][0]
        queue.appendleft(houses[0])
    if M == N:
        print(ans // M)
    else:
        print(ans)
