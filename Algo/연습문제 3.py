def make_star(n, V, adj_m):
    # stack 생성

    stack = []

    # visitied 생성

    visited = [0] * (V + 1)

    # 시작점 방문 표시

    visited[n] = 1

    # 각 정점에서 할일, do[n]

    print(n)

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
                print(n)

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

                break


# 1번부터 V번 정점
# E개의 간선


V, E = map(int, input().split())

arr = list(map(int, input().split()))

# 인접 매트릭스
adj_m = [[0] * (V + 1) for _ in range(V + 1)]

for i in range(E):
    v1, v2 = arr[i * 2], arr[i * 2 + 1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

print(adj_m)
make_star(1, V, adj_m)