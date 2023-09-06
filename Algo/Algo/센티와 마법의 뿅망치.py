import sys
import heapq
input = sys.stdin.readline()
n, h, t = map(int, input().split())
heap = []
for _ in range(n):
    a = int(input())
