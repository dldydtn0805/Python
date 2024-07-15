import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))

dp = [[1, [arr[i]]] for i in range(N)]
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            if dp[j][0] + 1 > dp[i][0]:
                dp[i][0] = dp[j][0] + 1
                dp[i][1] = dp[j][1] + [arr[i]]
ans = 0
ans_list = []
for i in range(N):
    if dp[i][0] > ans:
        ans = dp[i][0]
        ans_list = dp[i][1]
print(ans)
print(*ans_list)
