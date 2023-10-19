import sys
# sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())

arr1 = list(map(int, input().split()))

m = int(input())

arr2 = list(map(int, input().split()))

arr1.sort()

for a in arr2:
    start = 0
    end = n-1
    flag = 0
    while start <= end:
        mid = (start + end) // 2
        if arr1[mid] == a:
            flag = 1
            break
        elif arr1[mid] < a:
            start = mid + 1
        elif arr1[mid] > a:
            end = mid - 1
    if flag:
        print(1, end = ' ')
    else:
        print(0, end = ' ')