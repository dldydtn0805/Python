import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt')
input = sys.stdin.readline
n = int(input())
arr = [list(input()) for _ in range(n)]

temp = ''
result1 = ''
flag0 = 1
flag1 = 1
cnt = 0
def quadtree(n,x,y):
    global flag1, flag0, cnt


    if n == 1:
        if arr[x][y] == '1':
            flag0 = 0
        elif arr[x][y] == '0':
            flag1 = 0
        return


    quadtree(n//2, x, y)
    quadtree(n//2, x, y+n//2)
    quadtree(n//2, x+n//2, y)
    quadtree(n//2, x+n//2, y+n//2)


    if flag0:
        print(0)
    elif flag1:
        print(1)


    flag0 = 1
    flag1 = 1

quadtree(n, 0, 0)

'''
n = int(input())
board = [list(map(int, input())) for _ in range(n)]


def dfs(x, y, n):
    check = board[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != board[i][j]:
                check = -1
                break

    if check == -1:
        print("(", end='')
        n = n // 2
        dfs(x, y, n)  
        dfs(x, y + n, n) 
        dfs(x + n, y, n)  
        dfs(x + n, y + n, n)  
        print(")", end='')

    elif check == 1:
        print(1, end='')
    else:
        print(0, end='')

dfs(0, 0, n)
'''