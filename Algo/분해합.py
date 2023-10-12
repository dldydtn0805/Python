import sys
# sys.stdin = open('input.txt')
n = int(input())

r = 1e9
i = 1
while i <= 9*len(str(n)):
    A = n - i
    if A > 0:
        B = str(A)
        for b in B:
            A += int(b)
        if A == n:
            if r > int(B):
                r = int(B)
    i += 1
if r == 1e9:
    print(0)
else:
    print(r)