import sys
input = sys.stdin.readline

def get_count(string):
    cnt = 0
    for item in string:
        if int(item) % 2:
            cnt += 1
    return cnt

def divide_number_max(string):
    if len(string) == 1:
        return get_count(string)
    elif len(string) == 2:
        tmp = get_count(string)
        tmp += divide_number_max(str(int(string[0])+int(string[1])))
        return tmp
    else:
        max_v = 0
        for i in range(1, len(string)-1):
            for j in range(i+1, len(string)):
                tmp = get_count(string)
                tmp += divide_number_max(str(int(string[:i]) + int(string[i:j]) + int(string[j:])))
                max_v = max(max_v, tmp)
        return max_v


def divide_number_min(string):
    if len(string) == 1:
        return get_count(string)
    elif len(string) == 2:
        tmp = get_count(string)
        tmp += divide_number_min(str(int(string[0]) + int(string[1])))
        return tmp
    else:
        min_v = 1e9
        for i in range(1, len(string) - 1):
            for j in range(i + 1, len(string)):
                tmp = get_count(string)
                tmp += divide_number_min(str(int(string[:i]) + int(string[i:j]) + int(string[j:])))
                min_v = min(min_v, tmp)
        return min_v

N = input().rstrip()
print(divide_number_min(N), divide_number_max(N))
