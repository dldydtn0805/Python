def make_1(number):
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] =
    for i in range(2,n+1):
        if number - dp[i]
            dp[i] = dp[i-1]
number = int(input())
n = 1
cnt = 0

