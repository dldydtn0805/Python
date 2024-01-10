import sys
n = int(input())
x = list(input())
for _ in range(n-1):
    y = list(input())
    for i in range(len(x)):
        if x[i] != y[i]:
            x[i] = '?'

print(''.join(x))