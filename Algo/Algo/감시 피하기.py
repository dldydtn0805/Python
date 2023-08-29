import sys
sys.stdin = open('input.txt')

def gamsi(i,j):
    temp = []
    for di, dj in [[1,0],[-1,0]]:
        for p in range(1,n):
            ni = i + di*p
            nj = j + dj*p
            if 0<=ni<n and 0<=nj<n:
                temp.append((ni,nj))
                if arr[ni][nj] == 'S':
                    while temp:
                        c, d = temp.pop()
                        # 세로방향 시선일 경우 1
                        if arr[c][d] == 'X':
                            arr[c][d] = 1
        temp = []
    temp = []
    for di, dj in [[0,-1],[0,1]]:
        for p in range(1,n):
            ni = i + di*p
            nj = j + dj*p
            if 0<=ni<n and 0<=nj<n:
                temp.append((ni,nj))
                if arr[ni][nj] == 'S':
                    while temp:
                        e, f = temp.pop()
                            # 가로세로방향 시선일 경우 3
                        if arr[e][f] == 1:
                            arr[e][f] = 3
                            # 가로 방향 시선일 경우 2
                        elif arr[e][f] == 'X':
                            arr[e][f] = 2
        temp = []


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(input().split()) for _ in range(n)]
    teacher = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'T':
                teacher.append((i,j))
    while teacher:
        a, b = teacher.pop()
        gamsi(a,b)
    print(arr)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 3:
                cnt += 1
                arr[i][j] = 0
                # 가로 먼저
                for di, dj in [[0,1],[0,-1]]:
                    for p in range(1,n):
                        ni = i + di*p
                        nj = j + dj*p
                        if 0<=ni<n and 0<=nj<n:
                            if arr[ni][nj] == 2:
                                arr[ni][nj] = 0
                            elif arr[ni][nj] == 'T':
                                break
                # 다음 세로
                for di, dj in [[1,0], [-1,0]]:
                    for p in range(1,n):
                        ni = i + di*p
                        nj = j + dj*p
                        if 0 <= ni < n and 0 <= nj < n:
                            if arr[ni][nj] == 1:
                                arr[ni][nj] = 0
                            elif arr[ni][nj] == 'T':
                                break
            elif arr[i][j] == 2:
                cnt += 1
                arr[i][j] = 0
                # 가로 먼저
                for di, dj in [[0,1],[0,-1]]:
                    for p in range(1,n):
                        ni = i + di*p
                        nj = j + dj*p
                        if 0<=ni<n and 0<=nj<n:
                            if arr[ni][nj] == 2:
                                arr[ni][nj] = 0
                            elif arr[ni][nj] == 'T':
                                break
                # 다음 세로
                for di, dj in [[1,0], [-1,0]]:
                    for p in range(1,n):
                        ni = i + di*p
                        nj = j + dj*p
                        if 0 <= ni < n and 0 <= nj < n:
                            if arr[ni][nj] == 1:
                                arr[ni][nj] = 0
                            elif arr[ni][nj] == 'T':
                                break

            elif arr[i][j] == 1:
                cnt += 1
                arr[i][j] = 0
                # 가로 먼저
                for di, dj in [[0,1],[0,-1]]:
                    for p in range(1,n):
                        ni = i + di*p
                        nj = j + dj*p
                        if 0<=ni<n and 0<=nj<n:
                            if arr[ni][nj] == 2:
                                arr[ni][nj] = 0
                            elif arr[ni][nj] == 'T':
                                break
                # 다음 세로
                for di, dj in [[1,0], [-1,0]]:
                    for p in range(1,n):
                        ni = i + di*p
                        nj = j + dj*p
                        if 0 <= ni < n and 0 <= nj < n:
                            if arr[ni][nj] == 1:
                                arr[ni][nj] = 0
                            elif arr[ni][nj] == 'T':
                                break
    #만약 붙어있다면 소용 없음
    flag = True
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'S':
                for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
                    ni = i + di
                    nj = j + dj
                    if 0<=ni<n and 0<=nj<n:
                        if arr[ni][nj] == 'T':
                            flag = False
    if flag and cnt<=3:
        print('YES')
    else:
        print('NO')




