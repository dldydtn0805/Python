import math, sys

def eratos(num):
    i = 2
    if i > num:
        return False
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True


# sys.stdin = open('input.txt')

n = int(input())

arr = list(map(int, input().split()))

cnt = 0
for num in arr:
    if eratos(num):
        cnt += 1
print(cnt)

