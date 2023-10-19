import sys
# sys.stdin =open('input.txt')

a, b, v = map(int, input().split())

days = (v-a) // (a-b) + 1


if a == v:
    print(1)
    exit()

if v-a < a-b:
    print(2)
    exit()

print(days)

