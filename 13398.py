import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [[0, 0]for _ in range(n)]
# Q1 : 가장 작은 값을 지무면 안되나?
# A1 : 마음대로 누적합을 끊을 수 있다.
# R1 : 따라서 가장 작은 값을 지운 것이 정답이 아닐 수 있다.
for i in range(n):
    if i == 0:
        dp[i][0] = arr[0]
        dp[i][1] = arr[0]
    elif i == 1:
        dp[i][0] = max(dp[i-1][0] + arr[i], arr[i])
        dp[i][1] = dp[i-1][1] + arr[i]
    else:
        # 0에는 제거하지 않았을 경우를 담는다.
        # 1에는 한번 제거했을 경우를 담는다.
        dp[i][0] = max(dp[i-1][0] + arr[i], arr[i])
        dp[i][1] = max(dp[i-2][0] + arr[i], dp[i-1][1] + arr[i])
ans = -1*1e9
for i in range(n):
    ans = max(ans, dp[i][0], dp[i][1])
print(ans)
