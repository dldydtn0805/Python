import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

T = int(input())
for tc in range(1, T+1):
    K = int(input())
    # 이중 우선순위 큐 / 최대 힙, 최소 힙 두개로 구성
    max_queue = []
    min_queue = []
    # 각 힙을 연동 시키는 리스트
    is_deleted = [False] * K
    for k in range(K):
        process = input().split()
        # Input 의 경우 최대 힙은 (-정수, 인덱스), 최소 힙은 (정수, 인덱스)를 삽입한다
        if process[0] == 'I':
            heapq.heappush(min_queue, (int(process[1]), k))
            heapq.heappush(max_queue, (-int(process[1]), k))
        # Delete 의 경우
        elif process[0] == 'D':
            # 최소 힙 삭제 시키고 is_deleted[인덱스]를 True 전환
            if process[1] == '-1' and min_queue:
                poped_item = heapq.heappop(min_queue)
                is_deleted[poped_item[1]] = True
            # 최대힙 is_deleted[인덱스]를 True 전환
            elif process[1] == '1' and max_queue:
                poped_item = heapq.heappop(max_queue)
                is_deleted[poped_item[1]] = True
        #  각 힙을 연동 시키는 리스트[최소 값의 인덱스]가 True 라면 최소 값을 계속 삭제
        while max_queue and is_deleted[max_queue[0][1]] == True:
            heapq.heappop(max_queue)
        #  각 힙을 연동 시키는 리스트[최대 값의 인덱스]가 True 라면 최소 값을 계속 삭제
        while min_queue and is_deleted[min_queue[0][1]] == True:
            heapq.heappop(min_queue)
    if max_queue and min_queue:
        print(-heapq.heappop(max_queue)[0], end=' ')
        print(heapq.heappop(min_queue)[0])
    else:
        print('EMPTY')

