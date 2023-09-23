import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
n, m = map(int, input().split())
set = set()
for _ in range(n):
    set.add(input().rstrip())
    # print(set)
for _ in range(m):
    x = list(input().rstrip().split(','))
    # print(x)
    for i in x:
        set.discard(i)
    print(len(set))