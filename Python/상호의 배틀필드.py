import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    h, w = map(int, input().split())
    minimap = [list(input()) for _ in range(h)]
    n = int(input())
    order = list(input())
    di = [-1,0,1,0] #위 오른쪽 아래 왼쪽
    dj = [0,1,0,-1]
    while order:
        now = order.pop(0)
        # 현재 탱크 상태
        for i in range(h):
            for j in range(w):
                if minimap[i][j] in '<>^v':
                    ni, nj = i, j
                    sangtae = minimap[i][j]
        # 총 쏘기
        if now == 'S':
            if sangtae == '<':
                for p in range(1,n+1):
                    mj = nj + dj[3]*p
                    if 0<=mj<w:
                        if minimap[ni][mj] == '#':
                            break
                        elif minimap[ni][mj] == '*':
                            minimap[ni][mj] = '.'
                            break

            elif sangtae == '>':
                for p in range(1,n+1):
                    mj = nj + dj[1]*p
                    if 0<=mj<w:
                        if minimap[ni][mj] == '#':
                            break
                        elif minimap[ni][mj] == '*':
                            minimap[ni][mj] = '.'
                            break

            elif sangtae == '^':
                for p in range(1, n + 1):
                    mi = ni + di[0] * p
                    if 0 <= mi < h:
                        if minimap[mi][nj] == '#':
                            break
                        elif minimap[mi][nj] == '*':
                            minimap[mi][nj] = '.'
                            break
            elif sangtae == 'v':
                for p in range(1, n + 1):
                    mi = ni + di[2] * p
                    if 0 <= mi < h:
                        if minimap[mi][nj] == '#':
                            break
                        elif minimap[mi][nj] == '*':
                            minimap[mi][nj] = '.'
                            break
        # 이동하기
        if now == 'U':
            minimap[ni][nj] = '^'
            if 0 <= ni-1 < h:
                if minimap[ni-1][nj] == '.':
                    minimap[ni][nj] = '.'
                    minimap[ni-1][nj] = '^'

        if now == 'D':
            minimap[ni][nj] = 'v'
            if 0 <= ni+1 < h :
                if minimap[ni+1][nj] == '.':
                    minimap[ni][nj] = '.'
                    minimap[ni+1][nj] = 'v'

        if now == 'L':
            minimap[ni][nj] = '<'
            if 0<= nj-1 < w:
                if minimap[ni][nj-1] == '.':
                    minimap[ni][nj] = '.'
                    minimap[ni][nj-1] = '<'

        if now == 'R':
            minimap[ni][nj] = '>'
            if 0 <= nj+1 <w:
                if minimap[ni][nj+1] == '.':
                    minimap[ni][nj] = '.'
                    minimap[ni][nj+1] = '>'
    print(f'#{tc}', end=' ')
    for i in range(h):
        x = ''
        for j in range(w):
            x += minimap[i][j]
        print(x)
