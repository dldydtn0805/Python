import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def suffle(target, cnt):
    global max_cnt
    flag = True
    max_cnt = max(max_cnt, cnt)
    for i in range(len(target)):
        if target[i] % 3 != P[i]:
            flag = False
    if not flag:
        for i in range(len(target)):
            target[i] = S[target[i]]
        if target == copy:
            print(-1)
            exit()
        suffle(target, cnt+1)

N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))
target = [i for i in range(N)]
copy = target[:]
max_cnt = 0
suffle(target, 0)
print(max_cnt)
