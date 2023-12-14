import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
def make_star(cnt, cur, drink, value):
    global max_v
    if cnt == n:
        # print(value)
        if max_v < value:
            max_v = value
        return
    if drink == 2:
        make_star(cnt+1, cur+1, 0, value)
    if drink < 2:
        for i in range(cur, n):
            if visited[cnt] == 0:
                visited[cnt] = 1
                make_star(cnt+1, i+1, drink+1, value+table[i])
                visited[cnt] = 0
n = int(input())
table = [0]*n
for i in range(n):
    table[i] = int(input())
max_v = 0
visited = [0]*n
make_star(0, 0, 0, 0)
print(max_v)