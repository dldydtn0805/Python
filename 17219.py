import sys
input = sys.stdin.readline

dict = {}
N, M = map(int, input().rstrip().split())
for _ in range(N):
    url, pw = list(input().rstrip().split())
    dict[url] = pw
for _ in range(M):
    target = input().rstrip()
    print(dict[target])
