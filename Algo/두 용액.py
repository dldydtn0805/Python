import sys, heapq
sys.stdin = open('input.txt')

def binary2(start, end, target, temp):
    mid = (start + end) // 2
    if start > end:
        heapq.heappush(heap, [[abs(A[mid]+target)],[A[mid],target]])
        return
    if abs(A[mid] + target) > abs(temp) :
        binary2(start, mid - 1, target, A[mid]+target)
    elif abs(A[mid] + target) < abs(temp):
        binary2(mid + 1, end, target, A[mid]+target)
    elif abs(A[mid] + target) == abs(temp):
        heapq.heappush(heap, [[abs(A[mid] + target)], [A[mid], target]])
        return
n = int(input())
A = list(map(int, input().split()))
A.sort()
heap = []
for i in A:
    binary2(0,n-1, i, i)
print(heap)
print(*sorted(heapq.heappop(heap)[1]))