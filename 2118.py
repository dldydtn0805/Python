import sys
input = sys.stdin.readline

def binary_search():
    ans = 0
    for i in range(N):
        start, end = i, N-1
        while start <= end:
            mid = (start + end) // 2
            left = arr[mid] - arr[i-1]
            right = arr[N-1] - left
            if left < right:
                start = mid + 1
            else:
                end = mid - 1
            ans = max(ans, min(left, right))
    return ans

N = int(input())
arr = [int(input()) for _ in range(N)]
for i in range(1, N):
    arr[i] = arr[i-1] + arr[i]
print(binary_search())
