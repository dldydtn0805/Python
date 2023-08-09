import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    # 풍선
    ballons = [list(map(int, input().split())) for _ in range(n)]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    # 최대 꽃가루
    max_flower = 0
    for i in range(n):
        for j in range(m):
            # 꽃가루 개수
            sum_flower = ballons[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<= ni < n and 0<= nj < m: # 벽 세우기
                    sum_flower += ballons[ni][nj]
            max_flower = max(sum_flower, max_flower)
    print(f'#{tc}', max_flower)
