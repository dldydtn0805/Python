# 반복문
#
# arr = [2,4,7,9,11,19,23]
#
# arr.sort()
#
# def binarySearch(target):
#     low = 0
#     high = len(arr) - 1
#
#     # 인덱스가 꼬여버린 경우, 즉 low > high 라면 데이터를 못찾은 경우이다
#     while low <= high:
#         mid = (low + high) // 2
#
#         # 데이터를 찾은 경우
#         # 1. 가운데 값이 정답인 경우
#         if arr[mid] == target :
#             return mid
#         # 2. 가운데 값이 정답보다 작은 경우
#         elif arr[mid] < target :
#             low = mid + 1
#         # 3. 가운데 값이 정답보다 큰 경우
#         else :
#             high = mid - 1
#
#     return "해당 데이터는 없습니다"
#
# print(f'9 = {binarySearch(9)}')

# 재귀 호출

arr = [2,4,7,9,11,19,23]

arr.sort()
# 함수 한번 호출때마다 low, high 변수가 바뀌어서 사용됨
def binarySearch(low, high, target):
    # 기저조건 : 언제까지 재귀호출을 반복할 것인가?
    if low > high :
        return -1
    mid = (low + high) // 2
    # 기저조건을 먼저 생각해주고
    # 재귀를 안돌아도 될 경우를 먼저 작성한다
    # 다시한번 재귀 함수에 어떤 데이터를 주어야할지 고민
    # 1. 가운데 값이 정답인 경우
    if target == arr[mid]:
        return mid
    # 2. 가운데 값이 정답보다 작은 경우
    elif arr[mid] < target:
        return binarySearch(mid+1, high, target)
    # 3. 가운데 값이 정답보다 큰 경우
    else:
        return binarySearch(low, mid-1, target)

print(f'9 = {binarySearch(0, len(arr)-1, 9)}')
print(f'4 = {binarySearch(0, len(arr)-1, 4)}')
print(f'3 = {binarySearch(0, len(arr)-1, 3)}')


