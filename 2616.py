import sys
input = sys.stdin.readline

N = int(input())
trains = list(map(int, input().split()))
mini = int(input())
prefix = [0 for _ in range(N)]
for i in range(N):
    if i == 0:
        prefix[i] = trains[i]
    else:
        prefix[i] = prefix[i-1] + trains[i]
prefix = [0] + prefix
# dp[i][j]는 i번째 객차까지 고려했을때 j개의 소형 기관차를 사용한 경우의 최대 승객 수
dp = [[0]*3 for _ in range(len(prefix))]

for i in range(mini, len(prefix)):
    for j in range(3): # 1 , 2 , 3 번째 소형 기관차
        current_sum = prefix[i] - prefix[i-mini]
        if j == 0:
            dp[i][j] = max(dp[i-1][j], current_sum)
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-mini][j-1] + current_sum)
print(dp[-1][-1])
