import sys
sys.stdin = open('input.txt')

#최대값 함수
def max_V(X, Y):
    if X > Y:
        return X
    elif X < Y:
        return Y
    elif X == Y:
        return X

#이동하는 함수, position 현재 위치, K 최대 이동 거리, Station 충전소, N 종점
def move_position(position, K, station):
    # 범위에 있는 충전소 중에 최대한 갈수있는 충전소의 위치
    max_gas = 0
    # 충전소 순회하기
    for gas in station:
        # 현재위치와 최대로 갔을때의 위치 사이에 충전소가 있다면
        if position < gas <= position + K:
            # 충전소 위치 값들 중에 가장 먼 충전소가 최종적으로 저장된다
            max_gas = max_V(max_gas, gas)
    #만약 충전소가 한번도 없었다면 0을, 있었다면 최대한 갈 수 있는 위치값이 반환된다
    return max_gas

T = int(input())

for tc in range(1, T+1):
    #현재 정류장 위치
    position = 0
    K, N, M = map(int, input().split())
    # 충전소
    station = list(map(int, input().split()))
    total = 0
    while True:
        #만약, 갈수있는 위치에 충전소가 없다면, 탈락
        if move_position(position, K, station) == 0:
            total = 0
            break
        #만약, 충전소가 있다면, 최대로 이동할수있는 충전소로 이동시켜준다
        position = move_position(position, K, station)
        #이동 한 횟수가 추가된다
        total += 1
        #만약, 이제 충전소와 상관없이 현재 위치에서 최대로 이동할 수 있는 위치가 N보다 크다면, 도착한다.
        if position + K >= N:
            position = N
            break
    print(f'#{tc}', total)




