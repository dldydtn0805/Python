import sys
sys.stdin = open('input.txt')

#이동하는 함수, position 현재 위치, K 최대 이동 거리, Station 충전소, N 종점

def move_position(position, K, station):
    count = 0
    # 충전소 순회하기
    for gas in station:
        # 현재위치와 최대로 갔을때의 위치 사이에 충전소가 있다면,
        if position < gas <= position + K:
            #해당 충전소 위치를 반환한다
            count += 1
            return gas
    #만약 한번도 없었다면, False를 반환한다
    if count == 0:
        return False

T = int(input())

for tc in range(1, T+1):
    #현재 정류장 위치
    position = 0
    K, N, M = map(int, input().split())
    # 충전소
    station = list(map(int, input().split()))
    # print('테스트')

    check = True
    while check is True:
        #최대로 이동할수있는 충전소로 이동시켜준다
        position = move_position(position, K, station)
        #만약, 위치가 N보다 크다면, 도착
        if position + K >= N:
            position = N
            check = '도착'
            break
        #만약, 갈수있는 위치에 충전소가 없다면, 탈락
        if move_position(position, K, station) is False:
            check = '탈락'
            break
    print(check)



