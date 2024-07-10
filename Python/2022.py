import math

def binary_search(mid):
    h1 = math.sqrt(x * x - mid * mid)
    h2 = math.sqrt(y * y - mid * mid)
    return (h1 * h2) / (h1 + h2)

x, y, c = map(float, input().split())

start = 0
end = min(x, y)
ans = 0

while end - start > 0.000001:
    mid = (start + end) / 2.0

    if binary_search(mid) >= c:
        ans = mid
        start = mid
    else:
        end = mid

print(f"{ans:.3f}")
