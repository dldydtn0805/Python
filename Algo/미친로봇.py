import sys
# sys.stdin = open('input.txt')
def make_star(cnt,x,y,p):
    global n, result
    if visited[x][y] == 1:
        visited[x][y] += 1
        return
    visited[x][y] += 1
    if cnt == n:
        result += p
        return
    for k in range(4):
        if percent[k]:
            ni, nj, p = x  + di[k], y + dj[k], p * percent[k] / 100
            if 0<=ni<2*n+1 and 0<=nj<2*n+1:
                make_star(cnt+1, ni,nj, p)
                p = p / percent[k] * 100
                visited[ni][nj] -= 1

arr = list(map(int, input().split()))
n = arr[0]
percent = arr[1:] # 동서남북
space = [[0]*(2*n+1) for _ in range(2*n+1)]
visited = [[0]*(2*n+1) for _ in range(2*n+1)]
di = [0,0,1,-1] # 동서남북
dj = [1,-1,0,0] # 동서남북
result = 0
make_star(0,n,n,1)
print(result)