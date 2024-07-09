import sys
import heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

min_v = 1e9
for i in range(n-1):
    current = arr[i]

    start = i + 1
    end = n-1

    while start <= end:
        mid = (start+end) //2
        temp = current + arr[mid]

