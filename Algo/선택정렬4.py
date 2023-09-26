import heapq, sys
sys.stdin = open('input.txt')
def minus(A):
    A = A * -1
    return A
def selection_sort(A):
    cnt = 0
    for i in range(n-1, -1, -1):
        for j in range(i-1, -1, -1):




    #     if A[i] != min_v:
    #         cnt += 1
    # if cnt < k:
    #     print(-1)
    # else:
    #     print(A)
n, k = map(int, input().split())
A = list(map(int, input().split()))
B = sorted(A)
result = []
selection_sort(A)
print(B)
print(A)