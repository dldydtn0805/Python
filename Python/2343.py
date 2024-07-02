import sys
input = sys.stdin.readline

def can_record(size):
    count = 1
    cur_sum = 0
    for ele in arr:
        if cur_sum + ele > size:
            count += 1
            cur_sum = ele
        else:
            cur_sum += ele
        if count > M:
            return False
    return True

def binary_search(s, e):
    ans = e
    while s <= e:
        m = (s + e ) // 2
        if can_record(m):
            ans = m
            e = m-1
        else:
            s = m+1
    return ans

N, M = map(int, input().split())
arr = list(map(int, input().split()))

s = max(arr)
e = sum(arr)

print(binary_search(s, e))
