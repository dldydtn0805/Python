T = int(input())
dp = [0] * 101
for i in range(len(dp)):
    if i == 0 or i == 1 or i == 2:
        dp[i] = 1
    elif i==3 or i == 4:
        dp[i] = 2
    else:
        dp[i] = dp[i-1] + dp[i-5]
for _ in range(T):
    N = int(input())
    print(dp[N-1])
