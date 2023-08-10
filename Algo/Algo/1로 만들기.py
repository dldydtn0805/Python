import sys
sys.stdin = open('input.txt')

def make_number(number):
    dp = [0]*(number+1)
    dp[0] = 1
    for i in range(1,number+1):
        dp[i] = dp[i-1] + 1
        if dp[i] < number:
            dp[i] = max(dp[i-1]*2, dp[i])
            dp[i] = max(dp[i-1]*3, dp[i])
        if dp[i] == number:
            return i

number = int(input())
print(make_number(number))
