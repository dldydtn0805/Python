def check(num):
    tmp = str(num)
    if len(tmp) > 1:
        memo = int(tmp[1]) - int(tmp[0])
        for i in range(2, len(tmp)):
            if int(tmp[i]) - int(tmp[i-1]) != memo:
                return False
    return True
ans = [0 for _ in range(1001)]
N = int(input())
ans[1] = 1
for i in range(2, 1001):
    if check(i):
        ans[i] = ans[i-1] + 1
    else:
        ans[i] = ans[i-1]
print(ans[N])
