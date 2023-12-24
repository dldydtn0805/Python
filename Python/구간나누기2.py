"""
구간을 m개로 분할하고

각 구간에서 가장 큰값과 가장 작은 값이 있을텐데 그 차이가 value 이다

모든 m개의 구간의 value 들 중에서 가장 큰 수가 max_value인데

이 max_value들 중에 가장 작은 수를 찾아보자...

이걸 이분탐색으로 어케함?

"""


def binary(start, end):
    cnt = 0
    while start <= end:
        cnt += 1
        temp = 0
        mid = (start+end)//2

    return temp

import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())

arr = list(map(int, input().split()))

print(binary(0,n-1))