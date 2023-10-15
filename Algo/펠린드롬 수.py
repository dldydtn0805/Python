import sys
# sys.stdin = open('input.txt')

while True:
    temp = int(input())
    if temp:
        if str(temp) == str(temp)[::-1]:
            print('yes')
        else:
            print('no')
    else:
        break


