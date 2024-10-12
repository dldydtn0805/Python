import math
from functools import cache

@cache
def backtracking(depth, cur, rows, cols):
    if depth == N*M:
        global ans
        if cur:
            tmp = math.sqrt(int(cur))
            if (tmp.is_integer()):
                ans = max(ans, int(cur))
        return

    for i in range(N*M):
        if not visited[i//M][i%M]:
            if len(rows) >= 2 and len(cols) >= 2:
                if (int(rows[-1])-int(rows[-2]) == i//M-int(rows[-1])) and (int(cols[-1])-int(cols[-2]) == i%M - int(cols[-1])):
                    visited[i//M][i%M] = 1
                    backtracking(depth+1, cur+str(numbers[i//M][i%M]), rows+str(i//M), cols+str(i%M))
                    visited[i//M][i%M] = 0
            else:
                visited[i // M][i % M] = 1
                backtracking(depth + 1, cur + str(numbers[i // M][i % M]), rows + str(i // M), cols + str(i % M))
                visited[i // M][i % M] = 0
    backtracking(depth + 1, cur, rows, cols)


N, M = map(int, input().split())
numbers = [list(input()) for _ in range(N)]
ans = -1
visited= [[0 for _ in range(M) ]for _ in range(N)]
backtracking(0, '', '', '')
print(ans)
