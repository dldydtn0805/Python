import sys
# sys.stdin = open('input.txt')

string = list(input())

string.sort(reverse=True)

print(''.join(string))