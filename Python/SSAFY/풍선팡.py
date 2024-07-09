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
                # *range가 아래인 이유는, 풍선을 터트리면 각 방향으로 중심 꽃가루 개수 만큼의 범위의 풍선이 터지기 때문
                for p in range(1, ballons[i][j]+1):
                    ni = i + di[k]*p
                    nj = j + dj[k]*p
                    if 0<= ni < n and 0<= nj < m: # 벽 세우기
                        sum_flower += ballons[ni][nj]
            max_flower = max(sum_flower, max_flower)
    print(f'#{tc}', max_flower)
