import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(1001)]
for i in range(N+1):
    if i == 1: dp[i] = 1
    elif i == 2: dp[i] = 3
    else:
        dp[i] = dp[i-1] + 2*dp[i-2]
print(dp[N]%10007)
