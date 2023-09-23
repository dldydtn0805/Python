import sys
sys.stdin = open('input.txt')

def dfs(n, V, adj_m):
    route = []
    # stack 생성

    stack = []

    # visitied 생성

    visited = [0] * (V + 1)

    # 시작점 방문 표시

    visited[n] = 1

    # 각 정점에서 할일, do[n]

    route.append(n)

    while True:
        # 현재 정점 n에 인접하고 미방문 w 찾기
        for w in range(1, V+1):
            # 인접해있으면서
            # 방문한 적도 없음
            if adj_m[n][w] == 1 and visited[w] == 0:
                # push(n)
                stack.append(n)

                # n를 w로
                n = w

                # do(w)
                route.append(n)

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

                return route

for tc in range(1, 11):
    case, v = map(int, input().split())
    arr = list(map(int, input().split()))
    adj = [[0] * 100 for _ in range(100)]
    visited = [0] * (100)
    for i in range(0, len(arr)-1, 2):
        v1, v2 = arr[i], arr[i+1]
        adj[v1][v2] = 1
    result = dfs(0, 99, adj)
    # if 99 in result:
    #     print(f'#{tc}', 1)
    # else:
    #     print(f'#{tc}', 0)
    #
    print(result)