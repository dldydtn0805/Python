import sys
sys.stdin = open('input.txt')

def move_position(arr, number):

    # 현재 위치 설정
    ni = 0
    nj = 0
    # 각 방향으로 움직인 거리 설정
    left = 0
    right = 0
    down = 0
    # 탐색한 횟수 체크
    check = 0

    # 탐색 시작!
    while True:
    # 만약 현재 위치의 값이 2라면, 움직인 만큼 반환하고 함수 종료
        if 0 <= ni < number and 0 <= nj < number:
            if arr[ni][nj] == 2:
                return check + right - left
    # 만약, 현재 위치 기준 왼쪽 사다리가 1이고, 범위가 정상이라면 왼쪽 사다리로 이동
        if 0 <= nj-1 < number and arr[ni][nj-1] == 1:
            nj -= 1
            left += 1
    # 만약, 현재 위치 기준 오른쪽 사다리가 1이고, 범위가 정상이라면 오른쪽 사다리로 이동
        elif 0 <= nj+1 < number and arr[ni][nj+1] == 1:
            nj += 1
            right += 1

    # 아무튼 위의 작업 후에, 아래쪽 사다리로 이동
        ni += 1
        down += 1

    # 만약 다 내려왔고, 현재 위치의 값이 2가 아니라면, 탐색 횟수 추가하고 다음으로 넘어감
        if down == number:
            check += 1
            nj = check
            ni = 0
            left = 0
            right = 0
            down = 0
            continue
        if check > 100:
            break


for tc in range(1,11):
    n = input()
    arr = [list(map(int, input().split())) for _ in range(100)]
    print(move_position(arr, 100))