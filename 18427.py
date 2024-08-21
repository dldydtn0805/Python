import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M, H = map(int, input().split())
arr = [[0] + list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(H+1)] for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(H+1):
        if dp[i][j]:
            for k in arr[i]:
                if j + k <= H:
                    dp[i+1][j+k] = (dp[i][j] + dp[i+1][j+k]) % 10007

print(dp[N][H])

"""
1. dp[i][j]는 i번째 학생까지의 블록을 사용했을때 높이가 j인 탑을 만드는 경우의 수를 의미한다
2. dp[0][0]을 1로 초기화하여 기저 조건을 만족시킨다 [0번 학생까지 블록을 사용했을때 높이가 0인 탑을 만드는 경우의 수는 1이다]
3. 각 학생의 블록을 차례대로 고려하면서 dp[i][j]를 계산한다
4. dp[i][j]가 0이 아닌 경우, 현재 학생의 높이 k를 더해서 dp[i+1][j+k]에 결과를 누적한다 
[현재 학생 i의 블록 높이 k를 사용하여, 새로운 높이 j+k까지 만들 수 있는 경우의 수 dp[i+1][j+k]를 계산한다. 이때 이전 경우의 수 dp[i][j]와
현재까지 계산된 경우의 수 dp[i+1][j+k]를 더하여 누적한다]
5. 이 과정을 통해 dp[i+1][j+k]에는 i+1번쨰 학생까지의 블록을 사용하여 높이 j+k인 탑을 만드는 경우의 수가 저장된다
"""
