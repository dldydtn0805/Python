import sys
sys.stdin = open('input.txt')
T = int(input())
def dfs(cnt, i, j, sum_v):
    if cnt == 7:
        temp = ''.join(str(R))
        result.append(temp)
        return

    # 완전탐색
    for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
        ni, nj = di + i, dj + j
        if 0<= ni < 4 and 0<= nj < 4 :
            R.append(P[ni][nj])
            dfs(cnt+1, ni, nj, sum_v)
            R.pop()

for tc in range(1, T+1):
    P = [list(map(int, input().split())) for _ in range(4)]
    result = []
    R = []
    sum_v = ''
    for i in range(4):
        for j in range(4):
            visited = [[0] * 4 for _ in range(4)]
            dfs(0,i,j,sum_v)
    result = set(result)
    print(f'#{tc}', len(result))

