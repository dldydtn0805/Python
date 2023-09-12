import sys, heapq
input = sys.stdin.readline
# n은 선수의 수, k는 k년도 12월이 되었을때 팀의 선발 선수 가치의 합을 구해야하므로 선언
n, k = map(int, input().split())
# 11개 포지션의 선수들의 위치
heap = [[] for _ in range(11)]
# 포지션, 선수가치를 순차적으로 입력받아서 heap에 넣어준다 힙에 들어가는건 선수 가치 높은 순으로 정렬된다
for _ in range(n):
    p, w = map(int, input().split())
    heapq.heappush(heap[p-1], -w)
# k년 동안 11개 포지션을 순회하면서, 가장 가치가 높은 선수가 0보다 클때만 제일 비싼선수를 꺼내서 가치를 1 깎아준 다음 다시 넣어준다
for _ in range(k):
    for i in range(11):
        if heap[i] and heap[i][0] + 1 < 0:
            x = heapq.heappop(heap[i])
            heapq.heappush(heap[i], x+1)
result = 0
# 최종 선수 가치를 result 값에 넣어준다
for i in range(11):
    if heap[i]:
        x = -heap[i][0]
        result += x
print(result)