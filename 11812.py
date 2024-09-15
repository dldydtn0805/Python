import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def get_parents(X):
    if X == 1:
        return 1
    for i in range(len(prefix)):
        if prefix[i] < X:
            tmp = X - prefix[i - 1]
            if not (tmp % K):
                return prefix[i-2] + tmp // K
            else:
                return prefix[i-2] + (tmp // K) + 1

    tmp = X - prefix[i - 1]
    if not (tmp % K):
        return prefix[i - 2] + tmp // K
    else:
        return prefix[i - 2] + (tmp // K) + 1

def get_depth(X, Y):
    cnt = 0
    while X != Y:
        if X > Y:
            X = get_parents(X)
            cnt += 1
        elif X < Y:
            Y = get_parents(Y)
            cnt += 1

    return cnt

N, K, Q = map(int, input().split())

groups = []
total = 1
k = 0
if K == 1:
    for _ in range(Q):
        x, y = map(int, input().split())
        print(abs(x-y))
else:
    while total <= 10**15:
        groups.append(total)
        total *= K
    prefix = [0 for _ in range(len(groups))]

    for i in range(len(groups)):
        if i == 0:
            prefix[i] = groups[i]
        else:
            prefix[i] = prefix[i-1] + groups[i]

    prefix = [0] + prefix
    for _ in range(Q):
        x, y = map(int, input().split())
        print(get_depth(x, y))
