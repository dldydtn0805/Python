import sys
import sys; sys.stdin = open('input.txt')
from collections import defaultdict, deque

def find_max_depth(root, edges):
    # BFS로 각 별의 깊이를 찾음
    depth = [-1] * (len(edges) + 1)
    depth[root] = 0
    max_depth = 0
    queue = deque([root])

    while queue:
        node = queue.popleft()
        for neighbor in edges[node]:
            if depth[neighbor] == -1:
                depth[neighbor] = depth[node] + 1
                max_depth = max(max_depth, depth[neighbor])
                queue.append(neighbor)

    return max_depth

def min_constellation_length(N, decorations):
    edges = defaultdict(list)

    # 각 장식에 대한 연결 정보를 edges에 저장
    for i in range(N):
        A_i, *connections = decorations[i]
        for v, w in connections:
            edges[v].append(w)
            edges[w].append(v)

    # 첫 번째 장식에 대한 별자리 길이를 초기값으로 설정
    max_length = find_max_depth(1, edges)

    # 이후 장식들을 하나씩 추가하면서 별자리 길이 갱신
    for i in range(2, N + 1):
        max_length = max(max_length, find_max_depth(i, edges))

    return max_length + 1  # 별자리 길이는 깊이의 최댓값에 1을 더함

if __name__ == "__main__":
    N = int(input())
    decorations = []

    for _ in range(N):
        A_i = int(input())
        connections = [tuple(map(int, input().split())) for _ in range(A_i - 1)]
        decorations.append([A_i] + connections)

    result = min_constellation_length(N, decorations)
    print(result)
