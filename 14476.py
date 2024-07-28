import sys
input = sys.stdin.readline
import math


N = int(input())
arr = list(map(int, input().split()))
ans = -1
K = -1
L = [i for i in range(N)]
R = [i for i in range(N)]
for i in range(N):
    if i == 0:
        L[i] = arr[i]
    else:
        L[i] = math.gcd(L[i-1], arr[i])

for i in range(N-1, -1, -1):
    if i == N-1:
        R[i] = arr[i]
    else:
        R[i] = math.gcd(R[i+1], arr[i])
ans = -1
idx = -1
for i in range(N):
    if i == 0:
        cur = R[1]
    elif i == N-1:
        cur = R[N-2]
    else:
        cur = math.gcd(L[i-1], R[i+1])
    if arr[i] % cur:
        ans = max(ans, arr[i])
        idx = cur
if ans != -1:
    print(idx, ans)
else:
    print(-1)
