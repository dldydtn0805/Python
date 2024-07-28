# import sys
# sys.stdin = open('input.txt')

def bs(target, start, end):
    global f1, f2
    if start > end:
        return -1
    mid = (start + end) // 2
    if A[mid] == target:
        return mid

    elif A[mid] > target:
        if f1:
            return -1
        f1 = 1
        f2 = 0
        return bs(target, start, mid - 1)
    elif A[mid] < target:
        if f2:
            return -1
        f2 = 1
        f1 = 0
        return bs(target, mid + 1, end)


T = int(input())
for i in range(1, T+1):
    n, m = map(int, input(). split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = sorted(A)
    cnt = 0
    for b in B:
        f1, f2 = 0, 0
        result = (bs(b, 0, len(A)-1))
        if result != -1:
            cnt += 1
    print(f'#{i} {cnt}')

