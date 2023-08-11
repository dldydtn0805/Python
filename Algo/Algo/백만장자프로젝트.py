import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    arr = list(map(int, input().split()))
    total = 0
    basket = 0
    # 정방향
    while len(arr) > 0:
        x = max(arr)
        if arr[0] < x:
            basket += (x - arr[0])
        if arr[0] == x:
            total += basket
            basket = 0
        # 배열 없애기
        arr.pop(0)
    print(f'#{tc}', total)

