import sys
sys.stdin = open('input.txt')

n = int(input())
# 놀이판
playzone = [list(map(int, input().split())) for _ in range(n)]
stack = []
visited = [[0]*n for _ in range(n)]
# 오른쪽과 아래쪽으로만 이동
di = [0,1]
dj = [1,0]
# 시작점은 항상 0,0
i = 0
j = 0
# 방문 처리
stack.append((i,j))
visited[i][j] = 1
while True:
    # 오른쪽 아니면 아래쪽으로밖에 이동 못함
    for k in range(2):
        # 현재 값 만큼 점프!
        ni = i + di[k]*(playzone[i][j])
        nj = j + dj[k]*(playzone[i][j])
        # 점프한 위치가 정상이고, 방문한적 없었다면
        if 0<=ni<n and 0<=nj<n:
            if visited[ni][nj] == 0:
                # 스택에 넣어주고 방문 처리
                stack.append((ni,nj))
                visited[ni][nj] = 1
    # make_star 작동
    if stack:
        i, j = stack.pop()
    else:
        break
# 도착점은 항상 끝점
if visited[-1][-1] == 1:
    print('HaruHaru')
else:
    print('Hing')
