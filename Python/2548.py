import sys
input = sys.stdin.readline

def check(mid):
    tmp = 0
    for i in range(N):
        tmp += abs(arr[i] - arr[mid])
    if tmp <= ans[0]:
        ans[0] = tmp
        ans[1] = mid
        return True
    return False

def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2
        if check(mid):
            end = mid - 1
        else:
            start = mid + 1


N = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = [1e9, -1]
binary_search(0, N-1)
print(arr[ans[1]])
