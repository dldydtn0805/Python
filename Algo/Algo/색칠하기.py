# #교집합 되는 범위 구하는 함수
# def and22(x, y):
#     if x,

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    #N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질때
    #[x1, y1]에서 [x2, y2]까지 [color 1]으로 칠하라
    #arr = [x1,y1,x2,y2,color1]
    #arr를 N번 입력 받는다
    #색이 겹쳐 보라색이 된 칸 수를 구하라
    arr = [list(map(int, input().split())) for _ in range(N)]
    #배열을 새로 만들어야함
    #총 N번 만큼 배열을 만들기
    #총 색이 칠해진 개수를 count로 선언
    total = 0
    new_arr = [[0]*10 for _ in range(10)]
    for k in range(N):
        #new_arr은 10*10만큼의 크기를가지는 빈 팔렛트이다
        #빈 팔렛트에 arr에 설명에따라 색을 칠한다
        for i in range(arr[k][1], arr[k][3]+1):
            for j in range(arr[k][0], arr[k][2]+1):
                #new_arr가 비었을때, 해당하는 색을 칠한다
                if new_arr[i][j] == 0:
                    new_arr[i][j] = arr[k][4]
                #만약 비어있지 않을때, 칠해야하는 색과 다르다면, 보라색을 칠한다
                elif new_arr[i][j] != 0:
                    if new_arr[i][j] != arr[k][4]:
                        new_arr[i][j] = 3
                        total += 1
    print(f'#{tc}', total)


