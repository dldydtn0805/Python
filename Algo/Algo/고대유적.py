import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1+T):
    n, m = map(int, input().split())
    pic = [list(map(int, input().split())) for _ in range(n)]
    max_cnt = 0

    for i in range(n):
        cnt = 0
        for j in range(m):
            if pic[i][j] == 1:
                cnt += 1
                max_cnt = max(cnt, max_cnt)
            else:
                cnt = 0

    for i in range(m):
        cnt = 0
        for j in range(n):
            if pic[j][i] == 1:
                cnt += 1
                max_cnt = max(cnt, max_cnt)
            else:
                cnt = 0

    print(f'#{tc}',max_cnt)