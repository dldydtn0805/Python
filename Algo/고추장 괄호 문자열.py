import sys
# sys.stdin = open('input.txt')

# 괄호가 제대로 되어있는지 판단하는 함수
def check(G):
    stack = []
    for g in G:
        if g == '(':
            stack.append('(')
        else:
            if not stack:
                return 0
            if stack:
                stack.pop()
    if stack:
        return 0
    else:
        return 1

# 완전 탐색 브루트포스
def make_star(cnt):
    # cnt가 n이 됐을때 return을 하는데, 만약 괄호가 정상적이라면 해당 상황을 출력하고 프로그램을 종료한다
    if cnt == n:
        if check(G):
            result = ''.join(G)
            print(result)
            exit()
        return
    # 주어진 배열의 해당 요소가 고추장이라면, 완전탐색을 위해 해당 요소를 ')'와 '('로 넣어주고 make_star(cnt+1)을 호출
    if G[cnt] == 'G':
        for i in range(2):
            G[cnt] = sets[i]
            make_star(cnt+1)
            G[cnt] = 'G'
    # 고추장이 아니라면, 완전탐색을 위해 make_star(cnt+1)을 호출
    else:
        make_star(cnt+1)

n = int(input())
sets = ['(', ')']
G = list(input())
make_star(0)

