#버블 정렬 함수 구현
def sort_v(arr):
    # 맨 뒤에서 맨 앞으로 범위를 지정(i는 9, 8, 7, 6, 5, 4, 3, 2, 1)
    for i in range(len(arr)-1, 0, -1):
        # j는 i번 만큼 순회한다(9번, 8번, .... , 1번)
        for j in range(i):
            # 만약 배열의 j번째 값이 j+1번째 값보다 크다면 둘을 교환한다
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# import sys
# sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    sort_v(arr)
    print(f'#{tc}', *arr)
