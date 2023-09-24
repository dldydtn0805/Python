import sys
# sys.stdin = open('input.txt')

a, b, c = map(int, input(). split())

if c%2:
    a = a^b
print(a)