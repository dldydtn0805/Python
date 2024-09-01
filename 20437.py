import sys
input = sys.stdin.readline
from collections import defaultdict, deque

T = int(input())
for tc in range(T):
    W = list(input().rstrip())
    K = int(input())
    queues = defaultdict(deque)
    max_ans = defaultdict(int)
    min_ans = defaultdict(int)
    if K == 1:
        print(1, 1)
    else:
        for i in range(len(W)):
            if W[i] not in queues:
                queues[W[i]].append(i)
            else:
                queues[W[i]].append(i)
                if len(queues[W[i]]) == K:
                    front = queues[W[i]].popleft()
                    if not max_ans[W[i]] and not min_ans[W[i]]:
                        max_ans[W[i]] = i - front + 1
                        min_ans[W[i]] = i - front + 1
                    else:
                        max_ans[W[i]] = max(max_ans[W[i]], i - front + 1)
                        min_ans[W[i]] = min(min_ans[W[i]], i - front + 1)

        min_res = 1e9
        max_res = 0
        for min_v in min_ans.values():
            min_res = min(min_res, min_v)
        for max_v in max_ans.values():
            max_res = max(max_res, max_v)
        if max_res != 0 and min_res != 1e9:
            print(min_res, max_res)
        else:
            print(-1)
