import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(100)]

    # 출구의 행 인덱스[j]를 찾고 x로 정의해주기
    x = 0
    for j in range(100):
        if arr[99][j] == 2:
            x = j

    y = 99
    # y가 0이 되서 while 문 빠져나오는 순간 x값이 출발점
    while y > 0:

        #18번줄 # 만약 같은행 오른쪽 열의 값이 1이라면, 또 열이 99를 넘지 않았다면
        if (arr[y][x+1] == 1) and (x < 99) : # a = [1, 2, 3]일때 a[3]을 찾는건 오류다!
            # 그 조건이 계속 유지되는 한
            while (arr[y][x+1] == 1) and(x < 99):
                # 열의 값을 계속 1씩 계속 증가시킨다
                x += 1
                # print(x , end = ',')
            # 근데 오른쪽에 1이 없다면??? 위로 올라가야지 (왼쪽으로 다시 돌아가면 안되니깐)
            else:
                y -= 1
        # 28번줄

        # 만약 같은행 왼쪽 열의 값이 1이라면, 또 열이 99를 넘지 않았다면
        elif (arr[y][x-1] == 1) and (x > 1):
            # 그 조건이 계속 유지되는 한
            while (arr[y][x - 1] == 1) and (x > 1):
                # 열의 값을 계속 1씩 계속 감소시킨다
                x -= 1
            # 근데 왼쪽에 1이 없다면? 위로 올라가야지 (오른쪽으로 다시 돌아가면 안되니깐)
            else:
                y -= 1

        # 이 모든게 아니라면 당연히 위에 1이 있을수밖에 없으니깐
        else:
            # 위로 올라간다
            y -= 1
    # print()
    print(f'#{tc} {x}')