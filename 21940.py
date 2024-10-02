import sys
input = sys.stdin.readline

def floyd_warshall():
    dp = [[1e9 for _ in range(N+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        dp[i][i] = 0

    for i in range(1, N+1):
        for j in range(1, N+1):
            dp[i][j] = min(adj_list[i][j], dp[i][j])

    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                dp[i][j] = min(dp[i][k] + dp[k][j], dp[i][j])

    return dp

N, M = map(int, input().split())

adj_list = [[1e9 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    A, B, T = map(int, input().split())
    adj_list[A][B] = T
K = int(input())
C = list(map(int, input().split()))

distance = (floyd_warshall())

value = 1e9
ans = [0]
for city in range(1, N+1):
    time = 0
    for friend in C:
        time = max(time , distance[city][friend] + distance[friend][city])
    if value > time:
        value = time
        ans = [city]
    elif value == time:
        ans.append(city)
print(*sorted(ans))
