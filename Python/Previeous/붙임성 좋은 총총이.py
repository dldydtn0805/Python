import sys;
# sys.stdin = open('input.txt')
input = sys.stdin.readline
N = int(input())
dict = {}
dict['ChongChong'] = 1
for _ in range(N):
    man1, man2 = input().rstrip().split()
    if man1 in dict.keys():
        dict[man2] = 1
    if man2 in dict.keys():
        dict[man1] = 1

print(len(dict))

