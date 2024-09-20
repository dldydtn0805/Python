import sys, math, decimal
input = sys.stdin.readline

def get_num(X, Y):
    return math.floor(Y *100 / X)/100

X, Y = map(int, input().split())

start = 0
end = 10**9
ans = 10**10
while start <= end:
    mid = (start + end) // 2
    if decimal.Decimal(get_num(X, Y)) == decimal.Decimal(get_num(X+mid, Y+mid)):
        start = mid + 1
    else:
        ans = min(ans, mid)
        end = mid - 1
print(ans if ans != 10**10 else -1)
