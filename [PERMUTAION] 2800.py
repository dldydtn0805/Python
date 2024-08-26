import sys
input = sys.stdin.readline

def backtracking(max_depth, depth, idx):
    if depth == max_depth:
        unavail = set()
        for i in range(len(visited)):
            if visited[i]:
                l, r = total[i]
                unavail.add(l)
                unavail.add(r)
        ans = ''
        for i in range(len(arr)):
            if i not in unavail:
                ans += arr[i]
        res.append(ans)
    for i in range(idx, len(total)):
        visited[i] = 1
        backtracking(max_depth, depth + 1, i + 1)
        visited[i] = 0

arr = list(input().rstrip())
stack = []
total = set()
for i in range(len(arr)):
    cur = arr[i]
    if cur == '(':
        stack.append(i)
    elif cur == ')':
        total.add((stack.pop(), i))
total = list(total)

res = []

for i in range(len(total)):
    visited = [0 for _ in range(len(total))]
    backtracking(i + 1, 0, 0)

res = list(set(res))
res.sort()

for r in res:
    print(r)
