import sys
# sys.stdin = open('input.txt')

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
arr2 = list(map(int, input().split()))

for target in arr2:
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            print(1)
            break
        elif arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
    else:
        print(0)
            