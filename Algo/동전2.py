import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
n, k = map(int, input().split())
sample = []
for i in range(n):
    s = int(input().rstrip())
    # 각 샘플의 개수의 제한은 없고 n개의 종류가 주어지며 샘플을 더한 값이 k가 되어야 하는데,
    # 샘플 개수의 합이 최소가 되어야 한다
    # 이때 다이나믹 프로그래밍을 통해 구한다 치면,
    sample.append(s)
dp = [100001] * 10001
for i in range(n):
    if 10001 > sample[i]:
        dp[sample[i]] = 1
for i in range(min(sample), 10001):
    # 동일 종류 개수
    for j in range(n):
        if 10001 > sample[j] and dp[i] > dp[i- sample[j]]:
            dp[i] = dp[i - sample[j]] + 1
if dp[k] == 100001:
    print(-1)
    exit()
print(dp[k])

