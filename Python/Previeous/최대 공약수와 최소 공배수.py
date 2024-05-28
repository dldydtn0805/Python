import sys, math
# sys. stdin = open('input.txt')

n, m = map(int, input().split())

print(math.gcd(n,m))

print(math.lcm(n,m))