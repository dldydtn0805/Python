import sys

def bfs():
    for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
        for t in teacher:
            i, j = t
            ni = i + di
            nj = j + dj
            while 0<= ni < n and 0<= nj < n:
                if graph[ni][nj] == '0':
                    break
                if graph[ni][nj] == 'S':
                    return False

                ni += di
                nj += dj
    return True

def backtracking(cnt):
    global flag
    if cnt == 3:
        if bfs():
            flag = True
            return
    else:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'X':
                    graph[i][j] = 'O'
                    backtracking(cnt + 1)
                    graph[i][j] = 'X'



n = int(input())
teacher = []
graph = []
flag = False
for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j] == 'T': # 선생님 좌표 저장
            teacher.append((i,j))

backtracking(0)

if flag:
    print('y')
else:
    print('n')