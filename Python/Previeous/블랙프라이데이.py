import sys
# sys.stdin = open('input.txt')
sys.setrecursionlimit(10*9)

def binarySearch(start, end, c):
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == c:
            return mid
        if A[mid] < c:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def event(n, c):
    # 이진탐색으로 해당 값이 리스트에 있다 = 1개인 경우
    if binarySearch(0,n-1,c) >= 0:
        return True
    i = 0
    j = n-1
    while (i<j):
        sum_v = A[i] + A[j]
        if sum_v > c:
            j -= 1
        elif sum_v == c:
            #A[i], A[j] 조합
            return True
        else:
            # diff, A[i], A[j] 조합
            diff = c - sum_v
            if diff != A[i] and diff != A[j] and binarySearch(0, n-1, diff) >= 0:
                return True
            i+=1
    return False

n, c = map(int, input(). split())
A = list(map(int, input().split()))
A.sort()

if event(n, c):
    print(1)
else:
    print(0)