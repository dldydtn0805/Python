import sys, heapq
input = sys.stdin.readline
from collections import defaultdict
N = int(input())
heap = [[], []]
solved = defaultdict(int)
for _ in range(N):
    P, L = map(int, input().split())
    # L이 동일할때 P값이 더 작은 순서으로 꺼내진다
    heapq.heappush(heap[0], [L, P, solved[P]+1])
    heapq.heappush(heap[1], [-L, -P, solved[P]+1])
M = int(input())
for _ in range(M):
    command = list(input().rstrip().split())
    if command[0] == 'add':
        P, L = int(command[1]), int(command[2])
        # L이 동일할때 P값이 더 작은 순서으로 꺼내진다
        heapq.heappush(heap[0], [L, P, solved[P]+1])
        heapq.heappush(heap[1], [-L, -P, solved[P]+1])
    elif command[0] == 'recommend':
        if command[1] == '-1':
            # 만약 현재 가장 쉬운 문제가 이미 풀린 문제라면 그냥 꺼낸다
            while solved[heap[0][0][1]] >= heap[0][0][2]:
                heapq.heappop(heap[0])
            print(heap[0][0][1])
        else:
            # 만약 현재 가장 어려운 문제가 이미 풀린 문제라면 그냥 꺼낸다
            while solved[abs(heap[1][0][1])] >= heap[1][0][2]:
                heapq.heappop(heap[1])
            print(-heap[1][0][1])
    else:
        P = int(command[1])
        # solved[P] = 1 은 1번째 주어진 P를 해결했다는 의미이다
        solved[P] += 1
