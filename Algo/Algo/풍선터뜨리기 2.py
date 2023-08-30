import sys
from collections import deque
n = int(input())
# 풍선과 풍선의 인덱스를 따로 설정
arr = list(map(int, input().split()))
arr = deque(arr)
index = [i for i in range(1, n+1)]
index = deque(index)
# 인덱스가 터질때 담아줄 리스트 설정
temp = []
while arr:
    cnt = arr.popleft()
    x = index.popleft()
    temp.append(x)
    # 터진 풍선이 양수라면 오른쪽으로 이동해야한다
    if cnt > 0:
        arr.rotate(1-cnt)
        index.rotate(1-cnt)
    # 터진 풍선이 음수라면 왼쪽으로 이동해야한다
    else:
        arr.rotate(-cnt)
        index.rotate(-cnt)
print(*temp)