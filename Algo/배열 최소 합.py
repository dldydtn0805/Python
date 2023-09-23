import sys
sys.stdin = open('input.txt')

def search(col, cnt):
    global result

    if cnt > result: #현재 임시값이 최대값보다 크다면, 유망 x
        return

    if col == n:
        if cnt < result:
            result = cnt

    else:
        for row in range(n):
            if not visited[row]: #방문하지않은 열이라면,
                visited[row] = 1 #방문표시
                search(col+1, cnt+arr[col][row])
                visited[row] = 0 # 초기화





T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0]*n
    result = n * 10 * n

    search(0,0)
    print(result)