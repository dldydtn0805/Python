import sys
input = sys.stdin.readline
import heapq

T = int(input())
for tc in range(T):
    N = int(input())
    slimes = list(map(int, input().split()))
    heapq.heapify(slimes)
    ans = 1
    energy = []
    while slimes:
        tmp1 = heapq.heappop(slimes)
        if slimes:
            tmp2 = heapq.heappop(slimes)
            energy.append(tmp1*tmp2)
            heapq.heappush(slimes, tmp1*tmp2)
        else:
            break
    for e in energy:
        ans *= e
    print(ans%1000000007)
