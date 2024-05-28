import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = 0, 0
    n = int(input())
    dp = [0 for _ in range(n+1)]
    dp[0] = 0
    if n > 1:
        dp[1] = 1
    if n > 2:
        dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    elif n == 2:
        print(1, 1)
    else:
        print(dp[n-1], dp[n])