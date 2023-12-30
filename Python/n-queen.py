n = int(input())

ans = 0
checkboard = [0] * n

def backtracking(x):
    for i in range(x):
        # 같은 행이라면 불가능하므로 False
        # 대각선에 위치하면 불가능하므로 False
        if checkboard[x] == checkboard[i] or abs(checkboard[x] - checkboard[i]) == abs(x - i):
            return False
    return True


def dfs(x):
    global ans
    if x == n:
        ans += 1
        return
    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            checkboard[x] = i
            if backtracking(x):
                dfs(x + 1)
dfs(0)
print(ans)