import sys
input = sys.stdin.readline

N = int(input())
arr = []
dp = [[0, 0] for _ in range(N)]
for i in range(N-1):
    low, high = map(int, input().split())
    arr.append([low, high])

K = int(input())

for i in range(1, len(dp)):
    if i == 1:
        dp[1][0] = arr[0][0]
        dp[1][1] = 1e9
    elif i == 2:
        dp[2][0] = min(dp[1][0] + arr[1][0], dp[0][0] + arr[0][1])
        dp[2][1] = 1e9
    else:
        dp[i][0] = min(dp[i-1][0] + arr[i-1][0], dp[i-2][0] + arr[i-2][1])
        dp[i][1] = min(dp[i-1][1] + arr[i-1][0], dp[i-2][1] + arr[i-2][1], dp[i-3][0] + K)

print(min(dp[-1]))
