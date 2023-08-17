import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    index = [i+1 for i in range(m)]
    while True:
        for i in range(n):
            if len(arr) == 1:
                break
            print(arr)
            print(index)
            arr.append(arr.pop(0)//2)
            index.append(index.pop(0))
            if arr[-1] == 0:
                arr.pop()
                index.pop()
                if n < len(arr):
                    arr.append(arr.pop(n))
                    index.append(index.pop(n))

        if len(index) == 1:
            print(f'#{tc}', index.pop())
            break

