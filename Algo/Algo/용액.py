import sys
import heapq
input = sys.stdin.readline


n = int(input())
water = list(map(int, input().split()))
a, b = 0, 0
min_v = 1e9

def binary(start, end):
    mid = (start + end-1) // 2
    if min_v > water[mid]