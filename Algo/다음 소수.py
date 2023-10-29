import sys
import math
# sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    temp = int(input())
    flag = 0
    if temp == 0 or temp == 1 or temp == 2:
        print(2)
        continue
    if temp == 3:
        print(3)
        continue
    while flag == 0 :
        flag = 0
        for i in range(2, int(math.sqrt(temp))+1):
            if temp % i :
                flag = 1
            else:
                flag = 0
                break
        temp += 1
    print(temp-1)

