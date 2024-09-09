import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(33334)]
for i in range(2, len(dp)):
    if i == 2:
        dp[i] = 2
    else:
        dp[i] = dp[i-1] * 3
print(dp[N] % 1000000009)
