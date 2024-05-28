import sys
# sys.stdin = open('input.txt')

n = int(input())

arr = [0]*n

for i in range(n):
    arr[i] = int(input())

arr.sort()

for a in arr:
    print(a)