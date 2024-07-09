import sys
sys.stdin = open('input.txt')

# 만약 선생님의 상하좌우에 학생이 있으면 False를 반환하는 BFS
def bfs():
    for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
        for t in teacher:
            i, j = t
            ni = i + di
            nj = j + dj
            # 사각형 범위 안에서, 선생님 기준 상하좌우에 학생이 있는지 없는지 확인하는 while문
            while 0<= ni < n and 0<= nj < n:
                if arr[ni][nj] == 'O':
                    break
                if arr[ni][nj] == 'S':
                    return False
                ni += di
                nj += dj
    # 학생이 없었다면 True를 반환한다
    return True


def backtracking(cnt):
    global flag
    # 아래에서 O를 세개 체크하고 BFS를 돌려서 True가 반환되면 flag를 반환한다
    if cnt == 3:
        if bfs():
            flag = True
            return
    # 함수 시작하면 바로 장애물 설치한다
    else:
        # 전체 범위중에서 빈 곳을 찾아서 장애물을 설치하고 카운트를 1 올려서 함수를 재귀한다
        for i in range(n):
            for j in range(n):
                if arr[i][j] == 'X':
                    arr[i][j] = 'O'
                    # 카운트를 올려서 함수에 진입하면 다음 X에 O를 체크하게 된다
                    backtracking(cnt + 1)
                    # 다음 탐색으로 넘어가기 위해서 다시 X로 바꿔준다
                    arr[i][j] = 'X'


# T = int(input())
# for tc in range(1,T+1):
n = int(input())
teacher = []
flag = False
arr = [list(input().split()) for _ in range(n)]
# 선생님의 좌표 i, j를 뽑아서 teacher 에 넣어준다
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'T':
            teacher.append((i, j))

backtracking(0)

if flag:
    print('YES')
else:
    print('NO')