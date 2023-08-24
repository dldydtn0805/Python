import sys
sys.stdin = open('input.txt')

# N극
# 1 = n극
# 2 = s극
# S극
T = 10
for tc in range(1,T+1):
    n = int(input())
    desk = [list(map(int,input().split())) for _ in range(n)]
    # 교착 개수
    cnt = 0
    for i in range(n):
        now = 0
        for j in range(n):
            if desk[j][i] == 1:
                now = 1
            # 가장 최근에 지나친 자성체가 n극인 상태에서 현재 자성체가 s극이라면 교착 개수 추가
            if desk[j][i] == 2 and now:
                cnt += 1
                now = 0

    print(f'#{tc}', cnt)
