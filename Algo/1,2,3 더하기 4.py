import sys
sys.stdin = open('input.txt')


'''
0 -> 1 0 - > 1
1 -> 2 1 -> 1 + 1
2 - >3 1 + 1 -> 1 + 2 / 1 + 1 + 1
3 -> 4 1 + 2 + 1 / 1 + 1 + 1 + 1 / 1 + 3 / 2 + 2
4 - >5 1 + 2 + 1 + 1 / 1 + 1 + 1 + 1 + 1 / 1 + 3 + 1/ 2+ 2 + 1 / 3+ 2
0에서 1로 갈때 갯수는 1개 늘어남
1에서 2로 갈때 갯수는 그대로
2에서 3로 갈때 1개가 늘어남
3에서 4로 갈때 2개가 늘어남
4에서 5 로 갈때 1개가 늘어남

'''

t = int(input())

for tc in range(t):
    n = int(input())
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        if i < 6:
            dp[i] = i
        else:
            dp[i] = dp[i-6] + i
    print(dp[n])
    print(dp)