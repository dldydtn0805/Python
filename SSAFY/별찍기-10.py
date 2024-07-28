import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**9)

def make_star(x, y, N):
    # N이 1일 때 반환해야합니다! 더이상 나눌 수가 없읍니다 !
    if N == 1:
        return
    # 구간 범위 조정하는 x, y
    # 공백 범위 조정하는 N !
    for i in range(x+N//3, x+2*N//3):
        for j in range(y+N//3, y+2*N//3):
            stars[i][j] = ' '
    # 중심 제외 재귀
    # 11시
    make_star(x, y, N//3)
    # 12시
    make_star(x + N//3, y, N//3 )
    # 1시
    make_star(x + 2*N//3, y, N//3 )
    # 9시
    make_star(x, y+ N//3, N//3)
    # 3시
    make_star(x + 2*N//3, y+ N//3, N//3)
    # 7시
    make_star(x , y+ 2*N//3, N//3)
    # 6시
    make_star(x + N//3, y + 2 * N // 3, N // 3)
    # 5시
    make_star(x + 2*N // 3, y + 2 * N // 3, N // 3)

N = int(input())

stars = [[ '*' for i in range(N)] for j in range(N)]

make_star(0, 0, N)

for i in range(N):
    print(''.join(stars[i]))

