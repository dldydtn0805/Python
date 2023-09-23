import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):

    V, E = map(int, input().split())

    adj_m = [[0] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        v1, v2 = map(int, input().split())
        adj_m[v1][v2] = 1
    s, g = map(int, input().split())

    stack = []

    visited = [0] * (V + 1)

    visited[s] = 1

    while True:

        for w in range(1, V + 1):

            if adj_m[s][w] == 1 and visited[w] == 0:
                stack.append(s)
                s = w

                visited[s] = 1

                break

        else:

            if stack:
                s = stack.pop()

            else:
                break

    if visited[g]:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)