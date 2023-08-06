def bubble_sort(arr, N):
    # 버블 정렬은 i값이 역주행한다
    for i in range(N-1, 0, -1):
        # 끝까지 바꾸고, 끝-1까지, 끝-2까지, 끝-3까지, ..., 1까지 바꾼다
        for j in range(i):
            # j가 j+1보다 크면
            if arr[j] > arr[j+1]:
                # 연속한 두 값을 바꾼다
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def select_sort(arr, N):
    # i이 N까지 정주행한다
    for i in range(N):
        min_index = i
        # 1에서 N까지 바꾸고, 2에서 N까지 바꾸고, 3에서 N까지 바꾸고, ..., N에서 N까지 바꾸고
        for j in range(i, N):
            # j가 min_index 보다 작으면
            if arr[j] < arr[min_index]:
                # min_index 를 j로 바꾼다
                min_index = j
                # i와 min_index 위치를 바꾼다 **이게 핵심
                arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def counting_sort(arr):
    # 카운팅 배열 생성
    count_arr = [0]*(max(arr)+1)
    # arr 순회하면서 카운팅 배열에 추가
    for num in arr:
        count_arr[num] += 1
    # 카운팅 배열 누적해주기
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
    # result 초기화
    result = [0]*len(arr)
    # arr 순회하면서 result 에 정렬된 값 넣어주기
    for num in arr:
        # **count_arr[num]을 인덱스로 삼아서 정렬 시키고,
        idx = count_arr[num]
        result[idx-1] = num
        # **count_arr[num]값을 -1 해준다
        count_arr[num] -= 1

    return result

arr = [5,63,2,1,4,5,6]
N = 7
# result = bubble_sort(arr, N)
# result = select_sort(arr, N)
result = counting_sort(arr)
print(result)

