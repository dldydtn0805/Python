import sys
sys.stdin = open('input.txt')

n = int(input())
threesix = [str(i) for i in range(1,n+1)]
for i in threesix:
    if '3' in i:
        index = threesix.index(i)
        x = i.count('3')
        y = i.count('6')
        z = i.count('9')
        threesix.remove(i)
        threesix.insert(index, '-'*(x+y+z))

for i in threesix:
    if '6' in i:
        index = threesix.index(i)
        x = i.count('3')
        y = i.count('6')
        z = i.count('9')
        threesix.remove(i)
        threesix.insert(index, '-'*(x+y+z))

for i in threesix:
    if '9' in i:
        index = threesix.index(i)
        x = i.count('3')
        y = i.count('6')
        z = i.count('9')
        threesix.remove(i)
        threesix.insert(index, '-'*(x+y+z))

print(*threesix)