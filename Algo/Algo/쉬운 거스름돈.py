import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    dongzun = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    count = []
    for i in dongzun:
        if n // i:
            count.append(n//i)
        else:
            count.append(0)
        n %= i
    print(f'#{tc}')
    print(*count)
