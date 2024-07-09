import sys
n = int(input())
input = sys.stdin.readline
for _ in range(n):
    ans = 0
    strings = input()
    stack = 0
    for i in range(len(strings)):
        if strings[i] == 'O':
            stack += 1
            ans += stack
        else:
            stack = 0



    print(ans)