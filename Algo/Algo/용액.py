import sys
import heapq
input = sys.stdin.readline

n = int(input())
water = list(map(int, input().split()))
heap = [1e9]
