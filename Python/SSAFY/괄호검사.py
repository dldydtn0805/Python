import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    sentence = list(input())
    stack = []
    # now = 1, 정상 괄호 상태 / now = 0, 비정상 괄호 상태
    now = 1
    # 대응되는 괄호
    element_dic = {'}':'{', ')':'('}
    for element in sentence:
        # Push
        if element in ['{', '(']:
            stack.append(element)
        # Pop
        if element in ['}', ')']:
            if len(stack) > 0:
                if stack.pop() != element_dic[element]:
                    now = 0
            # 스택 길이가 0일때 닫는 괄호가 등장하면, 비정상 괄호 상태
            else:
                now = 0
    #  최종 스택 길이가 0이 아니면, 비정상 괄호 상태
    if len(stack) != 0:
        now = 0
    print(f'#{tc}', now)
