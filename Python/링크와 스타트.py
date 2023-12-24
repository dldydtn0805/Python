import sys
# sys.stdin = open('input.txt')

n = int(input())
stat = [list(map(int, input().split())) for _ in range(n)]
members = [i for i in range(n)]
min_v = 1e9
for i in range(1<<n):
    team_a = []
    team_b = []
    for j in range(n):
        if i & (1<<j):
            team_a.append(members[j])
    for i in members:
        if i not in team_a:
            team_b.append(i)
    if team_a == [] or team_b == []:
        continue

    sum_v_a = 0
    sum_v_b = 0
    for i in team_a:
        for j in team_a:
            sum_v_a += stat[i][j]
        # print(sum_v_a)
    for i in team_b:
        for j in team_b:
            sum_v_b += stat[i][j]
        # print(sum_v_b)
    min_v = min(min_v, abs(sum_v_a-sum_v_b))
    # print(team_a)
    # print(team_b)
print(min_v)