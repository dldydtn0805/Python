# import sys; sys.stdin = open('input.txt')
import math
a, b = map(int, input().split())
c, d = map(int, input().split())
x = (math.lcm(b, d))
y = ((x // b) * a + (x // d) * c)

z = (math.gcd(x,y))

print(y//z, x//z)