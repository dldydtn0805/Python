import sys
# sys.stdin = open('input.txt')

def dfs(cnt, cur):
    global max_v
    check = set(skill)
    now = 0
    if cnt == n:
        for q in quest:
            flag = 1
            for w in q:
                if w not in check:
                    flag = 0
            if flag:
                now += 1
        max_v = max(now, max_v)
        return

    for i in range(cur+1, 2*n+1):
        skill[cnt] = i
        dfs(cnt+1, i)

n, m, k = map(int, input().split())
quest = [list(map(int, input().split())) for _ in range(m)]
total = [i for i in range(1,2*n+1)]
skill = [0]*n
max_v = 0
dfs(0,0)
print(max_v)