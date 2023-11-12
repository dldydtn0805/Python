import sys;
# sys.stdin = open('input.txt')
input = sys.stdin.readline
N = int(input())
dict = {}
cnt = 0
for _ in range(N):
    joy = input().rstrip()
    if joy == 'ENTER':
        dict = {}
        continue
    if joy not in dict.keys():
        dict[joy] = 1
        cnt += 1
print(cnt)