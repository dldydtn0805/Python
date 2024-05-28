import sys; sys.stdin = open('input.txt')

x = input()

if x == '1 2 3 4 5 6 7 8':
    print('ascending')
elif x == '8 7 6 5 4 3 2 1':
    print('descending')
else:
    print('mixed')