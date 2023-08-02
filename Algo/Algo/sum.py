#비교함수 설정
def compare(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    elif x == y:
        return x

for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    #행 별 최대값 계산을 위해 변수를 설정
    total_row = 0
    for i in range(100):
        check = 0
        for j in range(100):
            check += arr[i][j]
        total_row = compare(total_row, check)
    #열 별 최대값 계산을 위해 변수를 설정
    total_col = 0
    for j in range(100):
        check = 0
        for i in range(100):
            check += arr[i][j]
        total_col = compare(total_col, check)
    compare_1 = compare(total_col, total_row)
    #대각선 최대값 계산을 위해 변수를 설정
    di = [-1,1,1,-1]
    dj = [1,1,-1,-1]
    totla_X = 0
    check = arr[50][50]
    for k in range(4):
        for m in range(1,24):
            ni = 50 + di[k]*m
            nj = 50 + dj[k]*m
            check += arr[ni][nj]
        total_X = compare(totla_X, check)
    compare_2 = compare(compare_1, total_X)
    print(f'#{tc}', compare_2)




