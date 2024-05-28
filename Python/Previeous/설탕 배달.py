import sys
sys.stdin = open('input.txt')

n = int(input())

dp = [0]*(n+1)
dp[3] = 1
dp[5] = 1
for i in range(3, n+1):
    if i % 3 == 0:
        dp[i] = dp[i-3] +1
    elif
    dp[i] = min((dp[i-3]+1), (dp[i-5]+1))
print(dp[n])