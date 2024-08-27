import sys
input = sys.stdin.readline

def get_value(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    current_value = 3
    i = 3
    range_size = 2
    flag = False
    while i <= n:
        next_i = i+ range_size
        if n < next_i:
            return current_value
        current_value += 1
        i = next_i
        if flag:
            range_size += 1
            flag = False
        else:
            flag = True

T = int(input())
for tc in range(T):
    x, y = map(int, input().split())
    print(get_value(y-x))
