# import sys
# sys.stdin = open('input.txt')

for tc in range(1,11):
    n = input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 현재 위치 찾아주기
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                ni = i
                nj = j

    # 사다리 오르기
    while True:
        ni -= 1
        while True:
            # 만약 현재 가로 위치가 1에서 99까지의 범위라면,
            if 0<= ni < 100 and 1 <= nj < 99:
                # 만약 왼쪽에 사다리가 있을때
                if arr[ni][nj-1] == 1:
                    # 왼쪽으로 이동하고, 이동하기 전의 사다리를 끊는다
                    arr[ni][nj] = 0
                    nj -= 1
                # 만약 오른쪽에 사다리가 있을때
                elif arr[ni][nj + 1] == 1:
                    # 오른쪽으로 이동하고, 이동하기 전의 사다리를 끊는다
                    arr[ni][nj] = 0
                    nj += 1
                # 위를 계속 반복하다보면, 왼쪽, 오른쪽에 사다리가 없는 상황이 생긴다, 이때 탈출한다
                else:
                    break
            # 만약 현재 가로 위치가 0이라면, 위의 반복문에서 왼쪽에 사다리가 있는 경우를 배제한다
            if nj  == 0:
                if arr[ni][nj + 1] == 1:
                    arr[ni][nj] = 0
                    nj += 1
                # 마찬가
                else:
                    break
            # 만약 현재 가로 위치가 99라면, 위의 반복문에서 오른쪽에 사다리가 있는 경우를 배제한다
            if nj == 99:
                if arr[ni][nj - 1] == 1:
                    arr[ni][nj] = 0
                    nj -= 1
                else:
                    break
        # 만약 현재 세로 위치가 0이라면, 도착!
        if ni == 0:
            print(f'#{tc}', nj)
            break
    #


