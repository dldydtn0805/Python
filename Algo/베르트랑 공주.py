import sys
# sys.stdin = open('input.txt')
import math
input = sys.stdin.readline

def checkSosu(num):
    cnt = 0
    temp = 2*num
    while num < temp:
        flag = 1
        num += 1
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                flag = 0
                break
        if flag == 1:
            cnt += 1
    return cnt
while True:
    n = int(input())
    if n == 0:
        break

    print(checkSosu(n))
