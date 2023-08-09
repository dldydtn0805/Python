"""
https://www.acmicpc.net/problem/1463

"""
import sys
sys.stdin = open('input.txt')

for tc in range(2):
    number = int(input())
    x = 1
    cnt = 0

    while x < number:

        x = x * 3
        cnt += 1

        if 3*x > number:
            x= x* 2
            cnt += 1

        elif 2*x > number:
            x= x+1
            cnt += 1


    print(cnt)



