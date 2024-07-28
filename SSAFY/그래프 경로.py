import sys
sys.stdin = open('input.txt')


def make_star(n, V, adj_m):
    arr = []

    # stack 생성

    stack = []

    # visitied 생성

    visited = [0] * (V + 1)

    # 시작점 방문 표시

    arr.append(n)

    visited[n] = 1

    while True:
        # 현재 정점 n에 인접하고 미방문 w 찾기
        for w in range(1, V + 1):
            # 인접해있으면서
            # 방문한 적도 없음
            if adj_m[n][w] == 1 and visited[w] == 0:
                # push(n)
                stack.append(n)

                # n를 w로
                n = w

                # do(w)
                arr.append(n)

                # visited[n]
                # w 방문 표시
                visited[n] = 1

                # 인접인 w를 찾았으니까 중단
                break

        # 현재 정점 n에서는 갈 w가 없어

        else:

            # stack에 정점이 남아있으면, 가장 마지막에 갔던 곳으로 돌아가기
            if stack:
                n = stack.pop()
            # stack이 정점이 비어있으면,

            else:

                # 전체 탐색이 끝났으니까 중단

                return arr


T = int(input())
for tc in range(1, T + 1):

    V, E = map(int, input().split())

    adj_m = [[0] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        v1, v2 = map(int, input().split())

        adj_m[v1][v2] = 1

        adj_m[v2][v1] = 1

    s, g = map(int, input().split())

    result = make_star(s, V, adj_m)

    # print(s,g, result)

    if s in result:
        result.remove(s)
    if g in result:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)