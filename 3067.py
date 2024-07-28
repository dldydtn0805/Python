import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    money = int(input())
    arr = [[0] for _ in range(N)]
    dp = [0 for _ in range(10001)]
    dp[0] = 1
    for price in prices:
        for i in range(price, money+1):
            dp[i] += dp[i-price]
    print(dp[money])
