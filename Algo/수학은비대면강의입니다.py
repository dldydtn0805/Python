import sys
# sys.stdin = open('input.txt')

a,b,c,d,e,f = map(int, input().split())
for x in range(-999, 1000):
    for y in range(-999, 1000):
        temp1 = a*x + b*y
        temp2 = d*x + e*y
        if temp1==c and temp2 == f:
            print(x, y)
            exit()
