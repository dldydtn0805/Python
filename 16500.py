S = input().rstrip()
N = int(input())
arr = [input().rstrip() for _ in range(N)]
dp = [0 for _ in range(len(S)+1)]
dp[0] = 1
for i in range(1, len(S)+1):
    for word in arr:
        if i >= len(word) and dp[i-len(word)] and S[i-len(word):i] == word:
            dp[i] = 1
print(dp[-1])
