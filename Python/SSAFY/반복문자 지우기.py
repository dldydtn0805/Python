import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    sentence = input()
    stack = []
    for element in sentence:
        stack.append(element)
        # 단어 길이 1 이상까지 반복
        if len(stack) > 1:
            # 방금 입력한 단어랑 원래 top이랑 같다면, 즉시 모두 삭제
            if stack[len(stack)-1] == stack[len(stack)-2]:
                stack.pop()
                stack.pop()
    print(f'#{tc}', len(stack))