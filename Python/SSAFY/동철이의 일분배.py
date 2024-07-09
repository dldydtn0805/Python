# import sys
# sys.stdin = open('input.txt')

def make_star(cnt, num):
    global max_v
    if cnt == N:
        max_v = max(max_v, num)
        return

    if max_v >= num:
        return

    for i in range(N):
        if SY[i] in ST:
            continue
        ST[cnt] = SY[i]
        make_star(cnt+1, num * PT[cnt][SY[i]-1]*0.01)
        ST[cnt] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    SY = [i for i in range(1, N+1)]
    ST = [0]*N
    PT = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    make_star(0,1)
    x = round(max_v*100,6)
    print(f'#{tc}', format(x, ".6f"))