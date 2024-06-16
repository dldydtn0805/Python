import sys
input = sys.stdin.readline

answer = []

def permutation(x, string_x, recursion_deepth):
    if recursion_deepth == m - 1:
        if string_x:
            answer.append(string_x + ' '+str(arr[x]))
        else:
            answer.append(str(arr[x]))
        return
    if string_x:
        result = string_x + ' ' + str(arr[x])
    else:
        result = str(arr[x])
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            permutation(i, result, recursion_deepth+1)
            visited[i] = False
n, m = map(int, input().split())
arr = list(map(int, input().split()))
visited = [False for _ in range(len(arr))]

for index in range(len(arr)):
    visited[index] = True
    permutation(index, '', 0)
    visited[index] = False
answer.sort(key=lambda x:[int(y) for y in x.split()])
for ans in answer:
    print(ans)
