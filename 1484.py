G = int(input())

start = 1
end = 1
ans = []
while end <= G:
    a = start**2
    b = end**2
    if b-a == G:
        ans.append(end)
        start += 1
    elif b-a < G:
        end += 1
    elif b-a > G:
        start += 1
if ans:
    for answer in ans:
        print(answer)
else:
    print(-1)
