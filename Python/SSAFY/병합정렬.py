
# import sys
# sys.stdin = open('input.txt')
#

def merge(left, right):
    global cnt
    result = [0]*(len(left)+len(right))
    left_i = 0
    right_i = 0
    i = 0
    # 한쪽이 빌때까지 반복
    if left[-1] > right[-1]:
        cnt += 1
    while len(left) > left_i or len(right) > right_i:
        if len(left) > left_i and len(right) > right_i:
            if left[left_i] <= right[right_i]:
                result[i] = left[left_i]
                i += 1
                left_i += 1
            else:
                result[i] = right[right_i]
                i += 1
                right_i += 1
        elif len(left) > left_i:
            result[i] = left[left_i]
            i += 1
            left_i += 1
        elif len(right) > right_i:
            result[i] = right[right_i]
            i += 1
            right_i += 1

    return result

def merge_sort(list):
    if len(list) == 1:
        return list
    middle = len(list) // 2
    left = list[:middle]
    right = list[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = merge_sort(arr)
    print(f'#{tc}', arr[n//2], cnt)