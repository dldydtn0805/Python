import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    rusia = [list(input()) for _ in range(n)]
    # W = 화이트
    # B = 블루
    # R = 레드
    # 순으로 최소 한줄은 칠해져야 한다
    min_v = 1e9
    w_cnt = 0
    for i in range(0, n-2):
        for j in range(m):
            if rusia[i][j] != 'W':
                w_cnt += 1
        b_cnt = 0
        for k in range(i+1, n-1):
            for g in range(m):
                if rusia[k][g] != 'B':
                    b_cnt += 1
            r_cnt = 0
            for l in range(k+1, n):
                for p in range(m):
                    if rusia[l][p] != 'R':
                        r_cnt += 1
            cnt = w_cnt + b_cnt + r_cnt
            min_v = min(cnt, min_v)
    print(f'#{tc}', min_v)
