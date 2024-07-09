import sys
# sys.stdin = open('input.txt')

L = int(input())

strings = list(input())

sum_v = 0
i = 0
while i < L:
    for string in strings:
        sum_v += (31**i)*(26 - (ord('z') - ord(string)))
        i += 1
print(sum_v%1234567891)