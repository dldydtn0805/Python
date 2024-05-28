import sys, heapq
# sys.stdin = open('input.txt')

input = sys.stdin.readline

heap = []
n = int(input())
for _ in range(n):
    heapq.heappush(heap, int(input()))

while heap:
    print(heapq.heappop(heap))