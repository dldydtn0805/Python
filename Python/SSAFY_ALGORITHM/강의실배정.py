import sys
import heapq

heap = []
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append([a,b])
arr.sort(key=lambda x:x[0]) #강의가 시작하는 시간을 기준으로 정렬
heapq.heappush(heap, arr[0][1]) # 첫번째 강의가 끝나는 시간을 넣음
for i in range(1,n):
    if heap[0] > arr[i][0]: #현재 강의가 끝나는 시간이 다음 강의 시작 시간 보다 늦게 끝난다면 다음 강의 끝나는 시간을 넣음
        heapq.heappush(heap,arr[i][1])
    else: #일찍 끝난다면 현재 강의실에서 해도 되므로 현재 강의실 자리에 다음 강의를 넣는다
        heapq.heappop(heap)
        heapq.heappush(heap,arr[i][1])
print(len(heap))