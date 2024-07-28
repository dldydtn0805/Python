import sys
input = sys.stdin.readline
from collections import defaultdict

string_dict = defaultdict(str)

def permutation(x, string_x, recursion_deepth):
    if recursion_deepth == m:
        string_dict[string_x] = 1
        return
    if string_x:
        result = string_x + ' ' + str(x+1)
    else:
        result = str(x+1)
    recursion_deepth += 1
    for i in range(x+1,len(arr)):
        permutation(i, result, recursion_deepth)
n, m = map(int, input().split())
arr = [i for i in range(n+1)]

for index in range(len(arr)):
    permutation(index, '', 0)

for ans in string_dict:
    print(ans)
