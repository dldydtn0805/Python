# import sys; sys.stdin = open('input.txt')
#
x = int(input())

n = 1
if x == 1:
    print('1/1')
    exit()
for i in range(0, 20000000):
    if n*(n+1)//2 == i:
        n += 1
        if x - i <= 0:
            break
        temp = i

if n % 2 :
    print(f'{x - temp}/{(i - temp + 1 - (x - temp))}')
else:
    print(f'{(i - temp + 1 - (x - temp))}/{x - temp}')

