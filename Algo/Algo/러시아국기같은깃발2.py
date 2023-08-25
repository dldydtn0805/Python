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
    cnt = 0
    for i in range(0, n-2):
        for k in range(i, n-1):
            for l in range(k, n):
                for j in range(m):
                    if rusia[i][j] != 'W':
                        cnt += 1
                    if rusia[k][j] != 'B':
                        cnt += 1
                    if rusia[l][j] != 'R':
                        cnt += 1
            min_v = min(cnt, min_v)
    print(min_v)
