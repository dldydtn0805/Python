N = int(input())
dp = [0 for _ in range(N)]
for i in range(N):
    arr = list(map(int, input().split()))
    번호, 시간 = i, arr[0]
    개수, 선행번호 = 0, []
    if 시간 : 개수 = arr[1]
    if 개수 : 선행번호 = arr[2:]
    if 선행번호 :
        for i in range(개수):
            dp[번호] = max(시간 + dp[선행번호[i]-1], dp[번호])
    else :
        dp[번호] = 시간
print(max(dp))
