N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

prefix_1 = [[0 for _ in range(M)] for _ in range(N)]
prefix_2 = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            prefix_1[i][j] = arr[i][j]
        elif i == 0:
            prefix_1[i][j] = prefix_1[i][j-1] + arr[i][j]
        elif j == 0:
            prefix_1[i][j] = prefix_1[i-1][j] + arr[i][j]
        else:
            prefix_1[i][j] = prefix_1[i][j-1] + prefix_1[i-1][j] + arr[i][j] - prefix_1[i-1][j-1]

for i in range(N-1, -1, -1):
    for j in range(M-1, -1, -1):
        if i == N-1 and j == M-1:
            prefix_2[i][j] = arr[i][j]
        elif i == N-1:
            prefix_2[i][j] = prefix_2[i][j+1] + arr[i][j]
        elif j == M-1:
            prefix_2[i][j] = prefix_2[i+1][j] + arr[i][j]
        else:
            prefix_2[i][j] = prefix_2[i][j+1] + prefix_2[i+1][j] + arr[i][j] - prefix_2[i+1][j+1]

# first case
ans = -1
for i in range(N):
    for j in range(M):
        tmp = prefix_1[i][j] * (prefix_1[i][M-1] - prefix_1[i][j]) * (prefix_1[N-1][M-1]-prefix_1[i][M-1])
        ans = max(tmp, ans)

for i in range(N-1, -1, -1):
    for j in range(M-1, -1, -1):
        tmp = prefix_2[i][j] * (prefix_2[i][0] - prefix_2[i][j]) * (prefix_2[0][0] - prefix_2[i][0])
        ans = max(tmp, ans)

for i in range(N):
    for j in range(M):
        tmp = prefix_1[i][j] * (prefix_1[-1][j] - prefix_1[i][j]) * (prefix_1[-1][-1] - prefix_1[-1][j])
        ans = max(tmp, ans)

for i in range(N-1, -1, -1):
    for j in range(M-1, -1, -1):
        tmp = prefix_2[i][j] * (prefix_2[0][j] - prefix_2[i][j]) * (prefix_2[0][0] - prefix_2[0][j])
        ans = max(tmp, ans)

for i in range(N-2):
    for j in range(i, N-1):
        for k in range(j, N):
            tmp = prefix_1[i][-1]*(prefix_1[j][-1]-prefix_1[i][-1])*(prefix_1[k][-1]-prefix_1[j][-1])
            ans = max(tmp, ans)

for i in range(M-2):
    for j in range(i, M-1):
        for k in range(j, M):
            tmp = prefix_1[-1][i]*(prefix_1[-1][j]-prefix_1[-1][i])*(prefix_1[-1][k]-prefix_1[-1][j])
            ans = max(tmp, ans)
print(ans)
