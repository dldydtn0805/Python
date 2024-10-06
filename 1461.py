def get_distance(X):
    dp = [1e9 for _ in range(len(X))]
    dp[0] = 2 * X[0]
    for i in range(len(X)):
        for j in range(M):
            pi = i - j - 1
            if 0 <= pi < len(X):
                dp[i] = min((dp[pi] + 2 * X[i]), 2 * dp[i])
    return dp
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

MINUS = get_distance(minus)
PLUS = get_distance(plus)

if minus[-1] > plus[-1]:
    print(MINUS[-1] + PLUS[-1] - minus[-1])
else:
    print(MINUS[-1] + PLUS[-1] - plus[-1])
