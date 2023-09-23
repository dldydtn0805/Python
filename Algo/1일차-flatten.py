
def maximum(x):
    max_arr = 0
    for i in range(len(x)): # 배열의 길이만큼 반복
        if arr[i] > max_arr: # 배열의 최고값 실시간 갱신
            max_arr = arr[i]

    return max_arr

def minimum(x):
    min_arr = 100
    for i in range(len(x)):  # 배열의 길이만큼 반복
        if arr[i] < min_arr:  # 배열의 최고값 실시간 갱신
            min_arr = arr[i]

    return min_arr

for tc in range(1, 11):
    count = int(input()) # 덤프하는 횟수
    arr = list(map(int, input().split())) # 배열 입력

    for j in range(count):

        max_idx = arr.index(maximum(arr))
        min_dix = arr.index(minimum(arr))
        arr[max_idx] -= 1
        arr[min_dix] += 1

    print(f'#{tc}', maximum(arr)- minimum(arr))

