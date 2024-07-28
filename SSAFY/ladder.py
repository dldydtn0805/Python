import sys
sys.stdin = open('input.txt')

def move_position(arr, number):

    # 현재 위치 설정
    ni = 0
    nj = 0
    # 각 방향으로 움직인 거리 설정
    left = 0
    right = 0

    # 탐색한 횟수 체크
    check = 0

    # 탐색 시작!
    while True:

    #만약 현재값이 0이라면, 오른쪽 사다리로 초기화해서 이동
        if arr[ni][nj] == 0:
            check += 1
            nj += check
            ni = 0
            right = 0
            left = 0
            continue

    # 만약 현재 값이 1이라면, 다음을 시행한다
        if arr[ni][nj] == 1:
        # 만약, 현재 위치 기준 왼쪽 사다리가 1이고, 범위가 정상이라면 왼쪽이 아닐때까지 왼쪽 사다리로 이동
            if arr[ni][nj-1] == 1:
                while arr[ni][nj-1] == 1:
                    nj -= 1
                    left += 1
        # 만약, 현재 위치 기준 오른쪽 사다리가 1이고, 범위가 정상이라면 오른쪽 사다리로 이동
            elif arr[ni][nj + 1] == 1:
                while arr[ni][nj + 1] == 1:
                    nj += 1
                    right += 1
            ni += 1

    # 만약, 위의 작업을 끝냈다면, 아래쪽 사다리로 이동
    # 만약 현재 위치의 값이 2라면, 움직인 만큼 반환하고 함수 종료
        if arr[ni][nj] == 2:
            return check

    # 만약 다 내려왔다면, 오른쪽 사다리로 초기화해서 이동
        if ni == number-1:
            check += 1
            nj = check
            ni = 0
            right = 0
            left = 0
            continue

for tc in range(1,11):
    n = input()
    arr = [list(map(int, input().split())) for _ in range(100)]
    print(move_position(arr, 100))