import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    # 출발점 찾기
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                a = i
                b = j
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    stack = []
    visited = [[0]*(n) for _ in range(n)]
    while True:
    # 현재 위치에서 순회하면서 만약 길이 열려있다면 방문하고 스택에 넣어줌
        for k in range(4):
            ni = a+di[k]
            nj = b+dj[k]
            if 0<= ni<n and 0<= nj<n:
                if arr[ni][nj] in [0,2,3] and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    stack.append((ni, nj))
    # 만약 스택이 0보다 크다면, 스택을 pop 하고 현재 위치를 갱신함
        if len(stack)>0:
            a, b = stack.pop()
    # 0이라면 탈출
        else:
            break
    #q, w는 탈출구의 위치
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 3:
                q, w = i , j
    #만약 탈출구를 방문했다면, 1을 출력
    if visited[q][w] == 1:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)