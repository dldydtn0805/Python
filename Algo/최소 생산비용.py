import sys
sys.stdin = open('input.txt')

def dfs(cnt):
    global sum_v, min_v

    if cnt == n:
        min_v = min(min_v, (sum_v))
        return

    if min_v < sum_v:
        return

    for i in range(n):
        if S[i] in P:
            continue
        P[cnt] = S[i]
        sum_v += F[cnt][S[i]-1]
        dfs(cnt+1)
        P[cnt] = 0
        sum_v -= F[cnt][S[i]-1]

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    S = [i for i in range(1, n+1)]
    P = [0]*n
    F = [list(map(int, input().split())) for _ in range(n)]
    min_v = 1e9
    sum_v = 0
    dfs(0)
    print(f'#{tc}', min_v)