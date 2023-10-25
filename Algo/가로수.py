import sys
sys.stdin = open('input.txt')

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

print(arr)