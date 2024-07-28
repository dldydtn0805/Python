N = int(input())
dp = [0 for _ in range(101)]
for i in range(1, 101):
    if i == 0:
        dp[i] = 1
    elif i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    elif i == 3:
        dp[i] = 3
    elif i == 4:
        dp[i] = 4
    elif i == 5:
        dp[i] = 5
    else:
        dp[i] = max(dp[i-3] + dp[i-3], dp[i-4] + 2*dp[i-4], dp[i-5] + 3*dp[i-5])
print(dp[N])
