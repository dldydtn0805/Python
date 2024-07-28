import sys
input = sys.stdin.readline

def backtracking(cnt, string):
    if cnt == N:
        ans.add(string)
        return
    else:
        for i in range(N):
            if not visited[i]:
                if string:
                    if string[-1] != S[i]:
                        visited[i] = 1
                        backtracking(cnt+1, string+S[i])
                        visited[i] = 0
                else:
                    visited[i] = 1
                    backtracking(cnt + 1, string + S[i])
                    visited[i] = 0

S = list(input().rstrip())
N = len(S)
ans = set()
visited = [0 for _ in range(N)]
backtracking(0, '')
print(len(ans))
