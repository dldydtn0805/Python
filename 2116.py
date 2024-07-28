N = int(input())
sum_dice = [0] * 6
case = [1, 2, 3, 4, 5, 6]

for _ in range(N):
    a, b, c, d, e, f = map(int, input().split())
    for i in range(6):
        cur = case[i]
        if cur == a:
            case[i] = f
            sum_dice[i] += max(max(b, c), max(d, e))
        elif cur == b:
            case[i] = d
            sum_dice[i] += max(max(a, c), max(e, f))
        elif cur == c:
            case[i] = e
            sum_dice[i] += max(max(a, b), max(d, f))
        elif cur == d:
            case[i] = b
            sum_dice[i] += max(max(a, c), max(e, f))
        elif cur == e:
            case[i] = c
            sum_dice[i] += max(max(a, b), max(d, f))
        else:
            case[i] = a
            sum_dice[i] += max(max(b, c), max(d, e))

print(max(sum_dice))
