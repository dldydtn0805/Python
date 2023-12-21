import sys
sys.stdin = open('input.txt')
from collections import deque
T = int(input())
for tc in range(1,T+1):
    p = list(input())
    n = int(input())
    numbers_origin = list(input())
    # 숫자를 파싱한 뒤에 담을 deque
    numbers_updated = deque()

    to_add_number = ''

    # to_add_number 라는 빈 문자열에 콤마(,)가 나오기 전까지 더해주고 콤마가 나오면 deque에 담는다
    for i in range(len(numbers_origin)):
        if numbers_origin[i].isnumeric():
            to_add_number = to_add_number + numbers_origin[i]
        elif numbers_origin[i] == ',':
            numbers_updated.append(to_add_number)
            # to_add_number 를 다시 빈 문자열로 초기화해준다
            to_add_number = ''
    # 빈 문자열은 추가하면 안되므 조건을 달아줘야한다
    if to_add_number != '':
        numbers_updated.append(to_add_number)
    # reverse flag 가 True 일때는 deque pop
    # reverse False 일때는 deque popleft
    reverse_flag = False
    error_flag = False
    for i in range(len(p)):
        if p[i] == 'R':
            if reverse_flag == False:
                reverse_flag = True
            else:
                reverse_flag = False
        else:
            # 함수 D 차례에 numbers_updated 가 비어있으면 에러 출력
            if not len(numbers_updated):
                print('error')
                error_flag = True
                break
            # 함수 D 차례에 numbers_updated가 비어있지 않고, reverse 가 False 라면 deque pop
            # 함수 D 차례에 reverse 가 True 라면 deque popleft
            else:
                if not reverse_flag:
                    numbers_updated.popleft()
                elif reverse_flag:
                    numbers_updated.pop()
    # error flag가 켜져있지 않을때만 최종 결과를 출력한다
    if not error_flag:
        if not reverse_flag:
            print('[', end='')
            for i in range(len(numbers_updated)):
                if i != len(numbers_updated)-1:
                    print(numbers_updated[i], end=',')
                else:
                    print(numbers_updated[i], end='')
            print(']', end='\n')
        else:
            numbers_updated.reverse()
            print('[', end='')
            for i in range(len(numbers_updated)):
                if i != len(numbers_updated) - 1:
                    print(numbers_updated[i], end=',')
                else:
                    print(numbers_updated[i], end='')
            print(']', end='\n')
