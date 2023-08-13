import sys
sys.stdin = open('input.txt')

"""
전체 탐색을 하면서 조건이 해당되는 상황에 플래그를 켜고

플래그가 켜졌다면, 최소 조건 출력

그게 아니라면 -1 출력
"""
N = int(input())

min_cnt = N
flag = 0
for a in range(N):
    cnt = N
    for b in range(N):
        if 5*a + 3*b == N:
            cnt = a + b
            flag = 1
    min_cnt = min(cnt, min_cnt)
if flag:
    print(min_cnt)
else:
    print(-1)