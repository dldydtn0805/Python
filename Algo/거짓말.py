import sys
# sys.stdin = open('input.txt')

n,m = map(int, input().split())
know_man = list(map(int, input().split()))
men = []
for _ in range(m):
    temp = list(map(int, input().split()))
    men.append(temp[1:])

x = set()
for t in know_man[1:]:
    x.add(t)

cnt = 0

tt = 0
while tt < 50:
    for i in men:
        flag = 1
        for j in i:
            if j in x:
                flag = 0
        if not flag:
            for j in i:
                x.add(j)
    tt += 1

for i in men:
    flag = 1
    for j in i:
        if j in x:
            flag = 0
    if flag:
        cnt += 1
print(cnt)