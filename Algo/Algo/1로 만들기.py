import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    def make_one(number):
        dp = [0]*(number+1)
        for i in range(2, number+1):
            dp[i] = dp[i-1] + 1
            if i % 2 == 0 :
                dp[i] = min(dp[i//2]+1, dp[i])
            if i % 3 == 0:
                dp[i] = min(dp[i//3]+1, dp[i])
        return dp[number]

    number = int(input())
    print(make_one(number))
