# import sys
# sys.stdin = open('input.txt')

#절대값 함수
def absolute(x, y):
    if x > y:
        return x - y
    elif x < y:
        return -(x - y)
    elif x == y:
        return 0

T = int(input())
for i in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 각각 배열의 최소, 최대값의 인덱스를 0번째라고 가정한다
    min_idx = 0
    max_idx = 0
    # 배열을 순회한다
    for j in range(N):
        #만약, 배열의 최소값이라고 지정된 변수보다 해당 인덱스의 배열 값이 더 작다면 최소값의 인덱스를 갱신한다
        if arr[min_idx] > arr[j]:
            min_idx = j
        #만약, 배열의 최대값이라고 지정된 변수보다 해당 인덱스의 배열 값이 더 크다면 최대값의 인덱스를 갱신한다
        #단, 최대값은 마지막에 나오는 위치로 하자고 했으므로, 같을때도 갱신한다
        if arr[max_idx] <= arr[j]:
            max_idx = j
    print(f'#{i}', absolute(max_idx, min_idx))