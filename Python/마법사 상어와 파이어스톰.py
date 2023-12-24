import sys
sys.stdin = open('input.txt')

n, q = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(2**n)]

l = list(map(int, input().split()))

print(arr)
print(l)