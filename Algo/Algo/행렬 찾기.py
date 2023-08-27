import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    di = [0,1] # 우, 하
    dj = [1,0]
    hang = [list(map(int, input().split())) for _ in range(n)]
    # 방문 했을때 표시
    visited = [[0]*n for _ in range(n)]
    # 출력하기 위해 마련
    result = []
    # 숫자가 0이 아닐때를 찾는다
    for i in range(n):
        for j in range(n):
            if hang[i][j] and not visited[i][j]:
                visited[i][j] = 1
                k = 0
                # 가로 먼저 늘려가면서 0이 나올때가지 체크한다
                while True:
                    nj = j + k
                    if hang[i][nj]:
                        k += 1
                    else:
                        break

                # 다음 세로 늘려 가면서 0이 나올때까지 체크한다
                p = 0
                while True:
                    ni = i + p
                    if hang[ni][j]:
                        p += 1
                    else:
                        break
                # 방문을 해서 다음 턴에 방문 안하도록 한다
                # 탐색한 범위에 행렬 전체 방문 표기
                # 계속 틀린 이유 p랑 k를 여기서 반대로 했음 ㅠㅠ
                for aa in range(i, i+p):
                    for bb in range(j, j+k):
                        if 0<=aa<n and 0<=bb<n:
                            visited[aa][bb] = 1
                temp = [(p)*(k), p, k]
                result.append(temp)
    result.sort()
    # 왜 중복이 돼서 담길까///// 방문을 중복으로 하는 경우가 있어서 ,,
    temp = []
    print(f'#{tc}', len(result), end = ' ')
    for i in range(len(result)):
        temp.extend(result[i][1:3])
    print(*temp)
