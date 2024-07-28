import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def star(x, y, cnt):
    if cnt == 0:
        arr[y][x] = '*'
        return
    tmp = 5**(N-cnt)
    star(x+2*tmp,y+0*tmp,cnt-1)
    star(x+2*tmp,y+1*tmp,cnt-1)
    star(x+0*tmp,y+2*tmp,cnt-1)
    star(x+1*tmp,y+2*tmp,cnt-1)
    star(x+2*tmp,y+2*tmp,cnt-1)
    star(x+3*tmp,y+2*tmp,cnt-1)
    star(x+4*tmp,y+2*tmp,cnt-1)
    star(x+1*tmp,y+3*tmp,cnt-1)
    star(x+2*tmp,y+3*tmp,cnt-1)
    star(x+3*tmp,y+3*tmp,cnt-1)
    star(x+1*tmp,y+4*tmp,cnt-1)
    star(x+3*tmp,y+4*tmp,cnt-1)

N = int(input())
arr = [[' ' for _ in range(5**N)] for _ in range(5**N)]
star(0, 0, N)
for i in range(len(arr)):
    print(''.join(arr[i]))
