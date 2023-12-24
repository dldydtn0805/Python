import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10*9)

def hoar_partition(arr, left, right):
    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i+1]
    return i+1

def quick_sort(arr, left, right):
    if left < right:
        pivot = hoar_partition(arr, left, right)
        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot +1, right)

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr) - 1)
    print(f'#{tc}', arr[n//2])
