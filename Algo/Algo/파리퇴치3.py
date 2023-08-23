import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    paris = [list(map(int, input().split())) for _ in range(n)]
    pi = [-1,0,1,0]
    pj = [0,1,0,-1]
    xi = [-1,1,1,-1]
    xj = [1,1,-1,-1]
    max_cut = 0
    for i in range(n):
        for j in range(n):
            cut = paris[i][j]
            for k in range(4):
                for p in range(1, m):
                    ni = i + pi[k]*p
                    nj = j + pj[k]*p
                    if 0<=ni<n and 0<=nj<n:
                        cut += paris[ni][nj]
            max_cut = max(cut, max_cut)

    max_cut2 = 0
    for i in range(n):
        for j in range(n):
            cut2 = paris[i][j]
            for k in range(4):
                for p in range(1, m):
                    ni = i + xi[k]*p
                    nj = j + xj[k]*p
                    if 0<=ni<n and 0<=nj<n:
                        cut2 += paris[ni][nj]
            max_cut2 = max(cut2, max_cut2)

    print(f'#{tc}', max(max_cut, max_cut2))