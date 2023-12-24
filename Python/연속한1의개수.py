# import sys
# sys.stdin = open('input.txt')

#최대값 함수 선언
def max_v(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return x

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 배열 변환 목적으로 문자열로 입력받는다
    string = input()
    # 정수형으로 변환한 상태로 배열로 전환한다
    arr = [int(string[i]) for i in range(N)]
    #check는 길이, max_check는 최대 길이이며 둘다 0이라고 설정한다
    max_check = 0
    check = 0
    for i in range(N):
        # 만약, 현재 인덱스의 값이 1이며 현재 길이가 0이라면, 길이는 1이다
        if  arr[i] == 1 and check == 0:
            check = 1
        # 그렇지 않고, 만약 현재 인덱스의 값이 1이고, 현재 길이가 0이 아니라면, 길이를 1 늘려준다
        elif arr[i] == 1 and check != 0:
            check += 1
        # 그렇지 않고, 만약 현재 인덱스의 값이 0이라면, 여태까지 모아놓은 길이를 최대 길이에 넣고, 길이를 초기화한다
        elif arr[i] == 0:
            max_check = max_v(max_check, check)
            check = 0
        # 위의 과정을 거친 후, 현재 인덱스의 값이 최종 값이라면, 여태까지 모아놓은 길이를 최대 길이에 넣고, 반복문을 마친다
        # 최종 값의 인덱스는 N-1이다
        if i == N-1:
            max_check = max_v(max_check, check)
    print(f'#{tc}', max_check)
