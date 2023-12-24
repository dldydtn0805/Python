import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt')
input = sys.stdin.readline
n = int(input())
arr = [list(input()) for _ in range(n)]

temp = []
result = []
flag0 = 1
flag1 = 1
cnt = 0
temp2 = []
def quadtree(n,x,y,):
    global flag1, flag0, cnt

    if n==1:
        temp.append(arr[x][y])
        return
    if len(temp) ==4:
        # print(temp)
        print('('*(n//2))
        if len(set(temp)) == 1:
            print(temp[0])
            temp2.append(temp[0])
        else:
            print(*temp)
        temp.clear()
        print(')'*(n//2))
    quadtree(n//2, x, y)
    quadtree(n//2, x, y+n//2)
    quadtree(n//2, x+n//2, y)
    quadtree(n//2, x+n//2, y+n//2)


quadtree(n, 0, 0)
print(result)
'''
n = int(input())
board = [list(map(int, input())) for _ in range(n)]


def make_star(x, y, n):
    check = board[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != board[i][j]:
                check = -1
                break

    if check == -1:
        print("(", end='')
        n = n // 2
        make_star(x, y, n)  
        make_star(x, y + n, n) 
        make_star(x + n, y, n)  
        make_star(x + n, y + n, n)  
        print(")", end='')

    elif check == 1:
        print(1, end='')
    else:
        print(0, end='')

make_star(0, 0, n)
'''