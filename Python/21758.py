import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

sum = arr[:]
ans = 0
for i in range(1, N):
    sum[i] += sum[i-1]

# 통 벌 벌
for i in range(1, N-1):
    ans = max(ans, sum[-2] + sum[i-1] - arr[i])

# 벌 벌 통

for i in range(1, N-1):
    ans = max(ans, sum[-1]-arr[0] + sum[-1]-sum[i] - arr[i])

# 벌 통 벌
for i in range(1, N-1):
    ans = max(ans, sum[-1]-arr[0]-arr[-1] + arr[i])

print(ans)
