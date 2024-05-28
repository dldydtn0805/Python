import sys, heapq, math
sys.stdin = open('input.txt')
def get_dist(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5
def djk():
    pass
start_i, start_j = map(float, input().split())
end_i, end_j = map(float, input().split())
n = int(input())
graph = [[0]*500 for _ in range(500)]
for _ in range(n):
    x, y = map(float, input().split())
