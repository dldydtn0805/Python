

import sys
sys.stdin = open('input.txt')

# 다이나믹 프로그래밍 함수
def Square(n):
# DP 배열
  dp = [0]*(n+1)
# 가로길이 n*10 만큼의 종이 채우기
  dp[0] = 0
  dp[1] = 1
  for i in range(2,n+1):
    if i % 2 == 1:
        dp[i] = 2*dp[i-1]-1
    if i % 2 == 0:
        dp[i] = 2*dp[i-1]+1
  return dp[n]

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    print(f'#{tc}', Square(n//10))

