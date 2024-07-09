import sys
# sys.stdin = open('input.txt')
n = int(input())
items = list(map(int, input().split()))
Dict = {}
for item in items:
    if item not in Dict:
        Dict[item] = 1
    else:
        Dict[item] += 1
ans = [0]*(n)
stack = []
for i in range(n-1, -1, -1):
    #역주행하면서 현재 숫자의 개수보다 적거나 같은 내역이 스택에 있으면 지워줍니다
    while stack and Dict[items[i]] >= Dict[stack[-1]]:
        stack.pop()
    #이 과정을 거치고도 스택에 숫자가 남아있으면서 가장 맨 위에있는 내역이라는 것은, 현재 숫자의 개수보다 크면서 가장 가까운 오른쪽에 있다는 것이므로 오등큰수 입니다
    if stack:
        ans[i] = stack[-1]
    #스택에 현재 숫자를 넣어줍니다
    stack.append(items[i])
for a in ans:
    if a == 0:
        print(-1, end=' ')
    else:
        print(a, end=' ')