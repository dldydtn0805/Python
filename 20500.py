N = int(input())
dp = [0 for i in range(N+1)]
for i in range(2, N+1):
    if i == 2 or i == 3:
        dp[i] = 1
    else:
        if i % 2 :
            dp[i] = 2* dp[i-1] - 1
        else:
            dp[i] = 2* dp[i-1] + 1
print(dp[N]%1000000007)
