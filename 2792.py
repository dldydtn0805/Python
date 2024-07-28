import sys
input = sys.stdin.readline

def can_divide(m):
    cnt = 0
    for i in range(M):
        if arr[i] <= m:
            cnt += 1
        else:
            if arr[i] % m:
                cnt += arr[i]//m+1
            else:
                cnt += arr[i]//m
    if cnt > N:
        return False
    return True

def binary_search(s, e):
    ans = e
    while s <= e:
        m = (s + e) // 2
        if can_divide(m):
            ans = m
            e = m-1
        else:
            s = m+1
    return ans

N, M = map(int, input().split())
arr = [int(input()) for _ in range(M)]
s = 1
e = max(arr)

print(binary_search(s, e))
