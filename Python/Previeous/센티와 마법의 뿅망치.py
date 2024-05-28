import sys
import heapq
input = sys.stdin.readline
n, h, t = map(int, input().split())
heap = []
# 음수로 넣으면 최대힙을 구할 수 있다
for _ in range(n):
    a = int(input())
    heapq.heappush(heap, -a)
# 때리는 횟수
cnt= 0
# 뿅망치 때리려면 횟수가 남아있어야하고, 최대힙이 1보다 커야하고, 최대힙이 센티보다 작거나 같아야한다
while t > cnt and 1 < -heap[0] and h <= -heap[0]:
    x = heapq.heappop(heap)
    cnt += 1
    # 음수로 계산중이므로 최대힙이 홀수일때는 1을 더해줘야 정상적인 몫이 나온다
    if x % 2:
        heapq.heappush(heap, x //2+1)
    else:
        heapq.heappush(heap, x//2)

# 최대힙보다 센티의 키가 크다면 몇번 때렸는지
if h > -heap[0]:
    print('YES')
    print(cnt)
# 그 외의 경우에는 최대힙을 반환한다
else:
    print('NO')
    print(-heap[0])