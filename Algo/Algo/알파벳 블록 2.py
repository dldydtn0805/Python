
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
n = int(input())
blog = []
number = []
stack = []
cnt = 0
for _ in range(n):
    button = list(input().split())
    if button[0] == '1':
        blog = blog + [button[1]]
        number = number + [cnt]
        stack.append((button[1], cnt))
        cnt += 1
    elif button[0] == '2':
        blog = [button[1]] + blog
        number = [cnt] + number
        stack.append((button[1], cnt))
        cnt += 1
    elif button[0] == '3' and stack:
        # x는 가장 최근에 삭제된 값 y는 지표
        x, y = stack.pop()
        i = 0
        while blog and number:
            if blog[i] == x and number[i] == y:
                # print(blog[i], number[i])
                blog.pop(i)
                number.pop(i)
                break

            i += 1


if blog:
    result = ''
    for i in blog:
        result += i
    print(result)
else:
    print(0)