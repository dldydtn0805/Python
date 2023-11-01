import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().strip().split()))
result = []
stack = []
for i in range(n):
    stack.append((i, arr[i]))
    while stack:
        if stack[-1][1] < arr[i]:
            stack.pop()
        else:
