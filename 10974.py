import sys
input = sys.stdin.readline

N = int(input())

visited = [0 for _ in range(N)]

def get_permutation(idx, ans):
    if idx == N:
        print(*ans)
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                get_permutation(idx+1, ans+[i+1])
                visited[i] = 0

get_permutation(0, [])
