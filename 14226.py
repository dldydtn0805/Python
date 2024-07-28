import sys
input = sys.stdin.readline
from collections import deque

def bfs(si):
    queue = deque()
    queue.append((si, 0))
    dp[si][0] = 0
    while queue:
        ci, c_clipboard = queue.popleft()
        c_value = dp[ci][c_clipboard]
        for ni in [ci+c_clipboard, ci-1]:
            if 0 <= ni < 2002:
                if dp[ni][c_clipboard] == -1:
                    queue.append((ni, c_clipboard))
                    dp[ni][c_clipboard] = dp[ci][c_clipboard] + 1

        if dp[ci][ci] == -1:
            queue.append((ci, ci))
            dp[ci][ci] = dp[ci][c_clipboard] + 1

S = int(input())
dp = [[-1 for _ in range(2002)] for _ in range(2002)]
bfs(1)
ans = 1e9
for i in range(len(dp[S])):
    if dp[S][i] != -1:
        ans = min(ans, dp[S][i])
print(ans)
