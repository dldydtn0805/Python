# import sys
# sys.stdin = open('input.txt')
# sys.setrecursionlimit(10**9)
def dfs(visit, cnt, value):
    global tc, min_v
    # 기저조건
    if visit == N-1:
        min_v = min(min_v, cnt)
        return
    if min_v < cnt:
        return
    for i in range(visit+1, visit+value+1):
        if 0<= i < len(M):
            dfs(i, cnt+1, M[i])

T = int(input())
for tc in range(1, T+1):
    B = list(map(int, input().split()))
    N = B[0]
    M = B[1:] + [0]
    min_v = 1e9
    dfs(0, -1, M[0])
    print(f'#{tc}', min_v)