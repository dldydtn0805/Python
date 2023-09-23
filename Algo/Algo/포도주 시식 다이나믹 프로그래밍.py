import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
n = int(input())
table = [0]*(10001)
for i in range(n):
    table[i] = int(input())

dp = [0]*(10001)
dp[0] = table[0]
dp[1] = table[0] + table[1]
result = dp[1]
for i in range(2,n):
    dp[i] = max(dp[i-2], dp[i-3]+table[i-1], dp[i-4]+table[i-1]) + table[i]
    if dp[i] > result:
        result = dp[i]
print(result)