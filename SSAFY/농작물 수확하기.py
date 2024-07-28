import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    n =int(input())
    nongjang = [list(input()) for _ in range(n)]
    # print(nongjang)
    tle = [[-1]*n for _ in range(n)]
    di = [-1,1,1,-1]
    dj = [1,1,-1,-1]
    for i in range(n):
        for j in range(n):
            # 가로 세로
            if i == n//2:
                tle[i][j] = 'x'
            if j == n//2:
                tle[i][j] = 'x'
    j = n//2
    x = 0
    while x < n//2:
        x += 1
        j -= 1
        for i in range(x, n-x):
            tle[i][j] = 'x'

    j = n
    x = n//2+1
    while x > 0:
        x -= 1
        j -= 1
        for i in range(x, n-x):
            tle[i][j] = 'x'
    sum = 0

    for i in range(n):
        for j in range(n):
            if tle[i][j] == 'x':
                sum += int(nongjang[i][j])
    print(f'#{tc}', sum)
