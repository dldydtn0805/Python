import sys
# sys.stdin = open('input.txt')

set = set()
s = list(input())
for i in range(len(s)):
    for j in range(len(s)):
        temp = ''.join(s[i:j+1])
        if temp:
            set.add(temp)
print(len(set))
