from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque()
    for idx, value in enumerate(priorities):
        queue.append([value, idx])
    cnt = 0
    def get(X): return X[0]
    while queue:
        if queue[0][0] != max(map(get, queue)):
            queue.append(queue.popleft())
        else:
            cnt += 1
            if location == queue.popleft()[1]:
                return cnt
    return cnt
