import sys
input = sys.stdin.readline

D, N = map(int, input().split())
cooker = list(map(int, input().split()))
pizza = list(map(int, input().split()))

dp = [0 for _ in range(D)]
for i in range(D):
    if i == 0:
        dp[i] = cooker[i]
    else:
        dp[i] = min(dp[i - 1], cooker[i])

ans = [0 for _ in range(N)]
j = 0
flag = False
for i in range(D-1, -1, -1):
    if dp[i] >= pizza[j]:
        ans[j] = i
        j += 1
        if j == N:
            flag = True
            break
if flag:
    for i in range(len(ans)-1, -1, -1):
        if ans[i]:
            print(ans[i]+1)
            break
    else:
        print(0)
else:
    print(0)
