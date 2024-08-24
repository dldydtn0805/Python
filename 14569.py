import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
classes = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
students = [list(map(int, input().split())) for _ in range(M)]
dict = defaultdict(set)
for i in range(len(students)):
    for j in range(1, len(students[i])):
        dict[i].add(students[i][j])

for s in range(len(students)):
    ans = 0
    for i in range(len(classes)):
        cnt = 0
        for j in range(1, len(classes[i])):
            if classes[i][j] in dict[s]:
                cnt += 1
        if cnt == classes[i][0]:
            ans+=1
    print(ans)
