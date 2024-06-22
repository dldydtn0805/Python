import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

def bfs(si, case):
    queue = deque()
    queue.append((si))
    visited = [0 for _ in range(N)]
    visited[(si)] = 1
    while queue:
        ci = queue.popleft()
        for ni in adjacent_list[ci]:
            if not visited[ni]:
                if ni in case:
                    queue.append(ni)
                    visited[ni] = 1
    if visited.count(1) == len(case): return True
    else: return False
N = int(input())
total_people = list(map(int, input().split()))
adjacent_list = [[] for _ in range(N)]
answer = 1e9
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(1, len(temp)):
        adjacent_list[i].append(temp[j]-1)

total_case = set()
for i in range(N):
    total_case.add(i)

answer = 1e9

for i in range(N):
    cases = list(combinations(total_case, i))
    for case in cases:
        counter_case = tuple(total_case.difference(case))
        if case and counter_case and bfs(case[0], case) and bfs(counter_case[0], counter_case):
            q_sum = 0
            w_sum = 0
            for q in range(len(case)):
                q_sum += total_people[case[q]]
            for w in range(len(counter_case)):
                w_sum += total_people[counter_case[w]]
            answer = min(answer, abs(q_sum-w_sum))

if answer != 1e9:
    print(answer)
else:
    print(-1)
