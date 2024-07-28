import sys;
# sys.stdin = open('input.txt')
from collections import deque
sys.setrecursionlimit(100000)

def make_star(si, sj, k):
    global flag
    # 만약 방문한적이 있으면 그냥 끝내고
    if (si, sj, k) in visited:
        flag = True
        # print(si, sj, k)
        return
    if not flag:
        visited.add((si, sj, k))
        # 맨 처음에서 => ni , nj로 이동
        # 해당 지점의 좌표값만큼 텔타 방향 이동을 함
        ni, nj = si + delta[k][0]*arr[si][sj], sj + delta[k][1]*arr[si][sj]
        # print(ni, nj)
        #만약 ni nj 범위가 정상이라면 진입하고
        if 0<= ni < N and 0<= nj< M:
        # 재귀함수로 진입
        # 불가능하다는건 오류가 난다는거임
        # 만약 k가 3이면 다시 0으로 만들고 재귀
            make_star(ni,nj, (k+1)%4)
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


#탈출한 별의 갯수를 구하면?
#탈출 못했을때 어떻게 판별할까??
delta = [[0,1], [1,0], [0,-1], [-1,0]]
ans = []
for i in range(N):
    flag = False
    # 각각 테이블이 무한 반복 가능한지 확인해야하므로
    visited = set()
    make_star(i, 0, 0)
    if flag:
        ans.append(i)
print(len(ans))
for i in range(len(ans)):
    print(ans[i]+1, end=' ')