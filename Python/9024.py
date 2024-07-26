import sys
input = sys.stdin.readline

def two_pointer(arr, K):
    i = 0
    j = len(arr)-1
    min_value = 1e9
    ans = 0
    while i < j:
        cur = arr[i] + arr[j]
        value = abs(cur-K)
        if value < min_value:
            min_value = value
            ans = 1
        elif value == min_value:
            ans += 1

        if cur < K:
            i += 1
        else:
            j -= 1

    return ans
T = int(input())
for tc in range(T):
    n, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    print(two_pointer(arr, K))
