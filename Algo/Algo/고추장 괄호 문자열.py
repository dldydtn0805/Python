from collections import deque
import sys
import itertools

sys.stdin = open('input.txt')

n = int(input())

sets = ['(', ')']

data = itertools.permutations(sets,2)

print(data)
G = list(input())
f1 = 0
f2 = 0
result = []
for i in G:
    result = []
    if i == 'G':
        result.append('(')

stack = []
for g in G:
    if g == 'G':
        if not stack:
            stack.append('(')
            f1 += 1
        else:
            if stack[-1] == '(':
                stack.append(')')
                f1 -= 1
            elif stack[-1] == ')':
                if f1 <= 0:
                    stack.append('(')
                    f1 += 1

                elif f1 > 0:
                    stack.append(')')
                    f1 -= 1

    else:
        stack.append(g)
        if g == ')':
            f1 -= 1
print(f1)
print(stack)