import sys
input = sys.stdin.readline

N = int(input())

dp = [0 for _ in range(31)]

for i in range(1, len(dp)):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 3
    else:
        dp[i] = dp[i-1] + 2 * dp[i-2]

if not N % 2:
    dp[N] = (dp[N] + dp[N//2] + 2 * dp[N//2-1]) // 2
else:
    dp[N] = (dp[N] + dp[N//2]) // 2

if N == 1:
    print(1)
elif N == 2:
    print(3)
else:
    print(dp[N])
