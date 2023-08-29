import sys
sys.stdin = open('input.txt')
for tc in range(1, 6):
    n = int(input())
    arr = list(map(int, input().split()))
    index = [i for i in range(n)]
    cnt = 0
    k = 0
    while arr:
        k -= 1
        x = index.pop(cnt)
        print(x + 1, end = ' ')
        cnt = arr.pop(cnt)
        if len(arr) < 2:
            break
        else:
            if x + cnt + k > 0:
                cnt = (x + cnt + k) % len(arr)
            else:
                cnt = (abs(x + cnt + - 2)) % len(arr)
    print(index.pop() + 1, end = '')
    print()

