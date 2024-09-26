N = int(input())
arr = list(map(int, input().split()))
arr.sort()
start = 0
end = N-1
value = arr[start] + arr[end]
ans = value
while start+1 < end:
    front = arr[start+1] + arr[end]
    back = arr[start] + arr[end-1]
    if abs(front) < abs(back):
        if abs(front) < abs(value):
            value = front
        if abs(ans) > abs(value):
            ans = value
        start += 1
    else:
        if abs(back) < abs(value):
            value = back
        if abs(ans) > abs(value):
            ans = value
        end -= 1
print(ans)
