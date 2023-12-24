import sys
# sys.stdin = open('input.txt')

while True:
    a, b, c = map(int, input().split())
    flag = 0
    if a == 0 and b == 0 and c == 0:
        break
    if a**2 + b**2 == c**2:
        flag = 1
    elif b**2 + c**2 == a**2:
        flag = 1
    elif c ** 2 + a ** 2 == b**2:
        flag = 1
    if flag:
        print('right')
    else:
        print('wrong')