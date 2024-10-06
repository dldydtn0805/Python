import heapq
N, M = map(int,input().split())
books = list(map(int, input().split()))
plus = []
minus = []
for i in range(N):
    if books[i] > 0:
        plus.append(books[i])
    else:
        minus.append(-books[i])

plus.sort()
minus.sort()
minus = [0] + minus
plus = [0] + plus
minus_dp = [1e9 for _ in range(len(minus))]
minus_dp[0] = 2*minus[0]
for i in range(len(minus)):
    for j in range(M):
        pi = i - j -1
        if 0<=pi<len(minus):
            minus_dp[i] = min((minus_dp[pi] + 2 * minus[i]), 2*minus_dp[i])

plus_dp = [1e9 for _ in range(len(plus))]
plus_dp[0] = 2*plus[0]
for i in range(len(plus)):
    for j in range(M):
        pi = i - j - 1
        if 0<=pi<len(plus):
            plus_dp[i] = min((plus_dp[pi] + 2 * plus[i]), 2*plus_dp[i])


if minus[-1] > plus[-1]:
    print(minus_dp[-1] + plus_dp[-1] - minus[-1])
else:
    print(minus_dp[-1] + plus_dp[-1] - plus[-1])
