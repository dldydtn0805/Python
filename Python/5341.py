import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N == 0:
        break
    else:
        print(sum([i for i in range(1, N+1)]))
