import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N):
    arr[i][0] = arr[i-1][0] + arr[i][0]
for j in range(1, M):
    arr[0][j] = arr[0][j-1] + arr[0][j]

for i in range(1, N):
    for j in range(1, M):
        arr[i][j] = arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1] + arr[i][j]
K = int(input())
for _ in range(K):
    x1,y1,x2,y2 = map(int, input().split())
    x1-=1
    y1-=1
    x2-=1
    y2-=1
    if not x1 and not y1:
        ans = arr[x2][y2]
    elif not x1:
        ans = arr[x2][y2] - arr[x2][y1-1]
    elif not y1:
        ans = arr[x2][y2] - arr[x1-1][y2]
    else:
        ans = arr[x2][y2] - arr[x1-1][y2] - arr[x2][y1-1] + arr[x1-1][y1-1]
    print(ans)
