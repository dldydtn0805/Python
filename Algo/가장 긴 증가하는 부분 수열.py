import sys
# sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))

dp = [0] * 1004
dp[0] = 1
for i in range(1, len(arr)):
    for j in range(0, i):
        if dp[i] <= dp[j] and arr[i] > arr[j]:
            dp[i] = max(dp[i] ,dp[j] + 1)
    if dp[i] == 0:
        dp[i] = 1
print(max(dp))