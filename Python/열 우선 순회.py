N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [0,1,0,-1]
dj = [1,0,-1,0]
m = 3 # 상하좌우 '두칸'까지! 탐색
max_v = 0 # 모든 원소가 0 이상이라면.

for i in range(N): #모든 원소 arr[i][j]에 대해.
    for j in range(N): #
        sum_v = 0
            for p in range(1,m):
                ni, nj = i+di[k]*p, j+dj[k]*p
                if 0<= ni < N and 0<= nj <N:
                    sum_v += arr[ni][nj]
        if max_v < sum_v:
            max_v = sum_v
print(max_v)