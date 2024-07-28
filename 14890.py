import sys
input = sys.stdin.readline

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    flag = True
    tmp = []
    for j in range(1, N):
        if arr[i][j-1] > arr[i][j]:
            same = []
            for k in range(L):
                if j + k >= N:
                    flag = False
                else:
                    if arr[i][j-1] - arr[i][j+k] > 1:
                        flag = False
                    else:
                        if same:
                            if arr[i][j+k] != same[0]:
                                flag = False
                        if j+k in tmp:
                            flag = False
                        else:
                            tmp.append(j+k)
                            same.append(arr[i][j+k])
        elif arr[i][j-1] < arr[i][j]:
            same = []
            for k in range(1, L+1):
                if j-k < 0:
                    flag = False
                else:

                    if arr[i][j] - arr[i][j-k] > 1:
                        flag = False
                    else:
                        if same:
                            if arr[i][j-k] != same[0]:
                                flag = False
                        if j-k in tmp:
                            flag = False
                        else:
                            tmp.append(j-k)
                            same.append(arr[i][j-k])
    if flag:
        ans += 1



for i in range(N):
    flag = True
    tmp = []
    for j in range(1, N):
        if arr[j-1][i] > arr[j][i]:
            same = []
            for k in range(L):
                if j + k >= N:
                    flag = False
                else:
                    if arr[j-1][i] - arr[j+k][i] > 1:
                        flag = False
                    else:
                        if same:
                            if arr[j+k][i] != same[0]:
                                flag = False
                        if j+k in tmp:
                            flag = False
                        else:
                            tmp.append(j+k)
                            same.append(arr[j+k][i])
        elif arr[j-1][i] < arr[j][i]:
            same = []
            for k in range(1, L+1):
                if j-k < 0:
                    flag = False
                else:

                    if arr[j][i] - arr[j-k][i] > 1:
                        flag = False
                    else:
                        if same:
                            if arr[j-k][i] != same[0]:
                                flag = False
                        if j-k in tmp:
                            flag = False
                        else:
                            tmp.append(j-k)
                            same.append(arr[j-k][i])
    if flag:
        ans += 1
print(ans)
