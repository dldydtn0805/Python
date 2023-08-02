def absoulte(x, y):
    if x > y:
        return x-y
    if x < y:
        return -(x-y)
    if x == y:
        return 0

T = int(input())
for tc in range(1, T+1):
    #5*5 2차 배열에 25개 숫자 초기화
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(5)]
    #25개의 각 요소에 대해 그 요소와 이웃한 요소와의 차의 절대값을 구하라
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    result = 0

    for i in range(n):
        for j in range(n):
            #4개의 방향으로 탐색한다
            for k in range(4):
                #탐색 대상 인덱스의 i, j값은 ni와 nj에
                ni = i+di[k]
                nj = j+dj[k]
                #가로 세로의 범위가 벗어나지 않도록 하자
                if 0 <= ni < n and 0 <= nj < n:
                    #기준 값과 비교 값의 차이는 몇일까, check 변수에 할당
                    check = absoulte(arr[i][j], arr[ni][nj])
            # 모조리 전부 다 최종 값에 더해준다
                    result += check #여기서 생각해야할 점은 네 방향으로 돌때 조건에 맞는다면, 즉시 result 값에 check를 더해줘야한다는 것이다
    print(f'#{tc}', result)