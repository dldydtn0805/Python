import sys
input = sys.stdin.readline
from itertools import combinations

def get_decreasing_numbers():
    numbers = []
    for i in range(1, 11):
        for comb in combinations(range(10), i):
            num = int(''.join(map(str, sorted(comb, reverse=True))))
            numbers.append(num)
    return sorted(numbers)

N = int(input())
decreasing_numbers = get_decreasing_numbers()
if N <= len(decreasing_numbers):
    print(decreasing_numbers[N-1])
else:
    print(-1)
