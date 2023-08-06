"""
스도쿠는 숫자퍼즐로, 가로 9칸 세로 9칸으로 이루어져 있는 표에 1부터 9까지의 숫자를 채워넣는 퍼즐이다
같은 줄에 1에서 9 까지의 숫자를 한번씩만 넣고, 3X3 크기의 작은 격자 또한 1에서 9까지의 숫자가 겹치지 않아야한다

입력으로 9X9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을때 위와같이 겹치는 숫자가 없을 경우,
1을 정답으로 출력하고, 그렇지 않을 경우 0을 출력한다

제약사항

퍼즐은 모두 숫자로 채워진 상태로 주어진다
입력으로 주어지는 퍼즐의 모든 숫자는 1이상 9 이하의 정수이다

입력

테스트 케이스는 9X9 크기의 퍼즐의 데이터이다
"""
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    check = True

    # 가로줄 탐색
    for i in range(9):
        tmp = [1,2,3,4,5,6,7,8,9]
        for j in range(9):
            # 만약 탐색하는데 숫자가 1~9 사이에 있다면,
            if arr[i][j] in tmp:
                # OK, 아무일도 일어나지 않는다, 해당 숫자를 tmp에서 삭제한다.
                tmp.remove(arr[i][j])
                pass
            # 만약 탐색하는데 숫자가 1~9 사이에 없다면, ( 위에서 삭제되었기 때문 )
            elif arr[i][j] not in tmp:
                check = False

    # 세로줄 탐색

    for i in range(9):
        tmp = [1,2,3,4,5,6,7,8,9]
        for j in range(9):
            # 만약 탐색하는데 숫자가 1~9 사이에 있다면,
            if arr[j][i] in tmp:
                # OK, 아무일도 일어나지 않는다, 해당 숫자를 tmp에서 삭제한다.
                tmp.remove(arr[j][i])
                pass
            # 만약 탐색하는데 숫자가 1~9 사이에 없다면, ( 위에서 삭제되었기 때문 )
            elif arr[j][i] not in tmp:
                check = False

    # 네모칸 탐색

    """
    탐색해야할 네모칸의 중심에 되는 좌표는 다음과 같다 
    이걸 k 반복문에 넣고 9번 돌리면 된다
    ni = [1,1,1,4,4,4,7,7,7] 
    nj = [1,4,7,1,4,7,1,4,7]
    9개 칸에 대해 설정해준다 # 자기 자신을 포함한다
    di = [-1,-1,-1,0,0,0,1,1,1] 
    dj = [-1,0,1,-1,0,1,-1,0,1]
    """
    for i in range(9):
        #자기 자신 좌표
        ni = [1, 1, 1, 4, 4, 4, 7, 7, 7]
        nj = [1, 4, 7, 1, 4, 7, 1, 4, 7]
        #자기 자신 포함해서 전 방향 탐색위한 좌표 설정
        di = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
        dj = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
        #자기 자신 포함해서 9칸씩 완전 탐색을 실시한다
        tmp = [1,2,3,4,5,6,7,8,9]
        for k in range(9):
            mi = ni[i] + di[k]
            mj = nj[i] + dj[k]
            # 만약, 해당 요소가 1~9 사이에 존재한다면,
            if arr[mi][mj] in tmp:
                tmp.remove(arr[mi][mj])
            # 만약, 해당 요소가 위에서 존재해서 삭제됐다면,
            elif arr[mi][mj] not in tmp:
                check = False

    #위의 과정을 다 거치고도 check가 True라면, 스도쿠는 문제가 없다.
    if check is True:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)