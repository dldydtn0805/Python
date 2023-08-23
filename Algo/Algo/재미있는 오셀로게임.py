import sys
sys.stdin = open('input.txt')

def bfs(i,j,color):
    # 해당하는 색의 돌을 둔다
    visited[i][j] = color
    # 큐에 방금 놓은 돌의 위치를 저장
    queue = []
    temp = []
    queue.append((i,j))
    di =[-1,-1,-1,1,1,1,0,0]
    dj =[0,1,-1,1,0,-1,-1,1]
    # 8개 방향에 대해서
    for k in range(8):
        ni = i + di[k]
        nj = j + dj[k]
        # 인접한 여덟 방향 위치가 정상이라면
        # 큐에 넣어주고
        queue.append((ni,nj))
        # 큐가 있는 동안
        while queue:
            a, b = queue.pop()
            # 돌이 없으면 정지
            if visited[a][b] == -1:
                break
            # 돌이 있으면 이동
            else:
                # 일단 큐에 위치 넣어주고
                queue.append((a,b))
                # 색이 다르다면 뒤집을 위치를 넣어준다
                if visited[a][b] != color:
                    temp.append((a,b))
                # 색이 같다면 뒤집어준다
                elif visited[a][b] == color:
                    while temp:
                        x, y = temp.pop()
                        visited[x][y] = color
                        print(visited)
    # 뒤집을 위치에 있는걸 다 꺼내주고 뒤집어준다
    # while temp:
    #     x, y = temp.pop(0)
    #     visited[x][y] = color

T = int(input())
for tc in range(1,T+1):
    n, m = map(int, input().split())
    # visited = 오셀로 판
    visited = [[-1] * (n) for _ in range(n)]
    visited[n//2-1][n//2-1] = 2
    visited[n//2-1][n//2] = 1
    visited[n//2][n//2-1] = 1
    visited[n//2][n//2] = 2
    # m번 입력 받음
    for _ in range(m):
        # 세로, 가로, 색깔
        i, j, color = map(int, input().split())
        bfs(i-1, j-1, color)

    a = 0
    b = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1:
                a += 1
            if visited[i][j] == 2:
                b += 1

    print(visited)
    print(f'#{tc}', a, b)

