import sys, math
# sys.stdin = open('input.txt')

x = str(math.factorial(int(input())))
cnt = 0
for i in range(len(x)-1, -1, -1):
    if x[i] != '0':
        break
    cnt += 1

print(cnt)
