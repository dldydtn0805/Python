import sys
sys.stdin = open('input.txt')
T = 2
for tc in range(1, T+1):
    n = int(input())
    distance = list(map(int, input().split()))
    gs = list(map(int, input().split()))
    total = sum(distance)
    # 뒤쪽에 있는 주유소 가격이 먼저있던 주유소 보다 더 저렴하다면, 해당 거리는 무조건 해당 주유소에서 채워야한다
    # 먼저 있는 주유소 가격이 더 저렴하다면, 미리 충전한다
    result = 0
    min_v = min(gs)
    min_gs = gs[0]
    for i in range(n-1):
        min_gs = min(min_gs, gs[i])
        result += min_gs*distance[i]
    print(result)
