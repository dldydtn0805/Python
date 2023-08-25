import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    haeng = [list(map(int, input().split())) for _ in range(n)]
    print(haeng)