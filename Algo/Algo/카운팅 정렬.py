# 입력 받은 배열
arr = [0,4,1,3,1,2,4,1]
# K 데이터 원소의 범위 (데이터의 갯수가 아님)
k = 5

# 원소의 등장 횟수 기록
# 배열의 정수 값을 인덱스로 가지는 카운트 배열 초기화
count_arr = [0]*(max(arr)+1)

# 배열의 정수값을 인덱스로하는 카운트 배열 갱신
for num in arr:
    count_arr[num] += 1

# 배열에 담긴 원소를 바로 정렬된 위치로 넣어주기 위한 사전 작업
for i in range(1, len(count_arr)):
    count_arr[i] += count_arr[i-1]

# result 배열에는 arr 배열의 원소를 정렬된 위치에 넣어줄 것
result = [0] * len(arr)
# arr 배열의 각 원소 값을 count 배열의 인덱스로 사용해 값을 가져온후에
# 다시 result 의 인덱스로 사용해 arr 의 원소로 저장한다
# 그리고 사용한 count 배열의 값을 1 줄여준다
for num in arr:
    idx = count_arr[num]
    result[idx-1] = num
    count_arr[num] -= 1
print(result)