"""
숫자 체계가 다른 행성, 이 행성에서 사용하는 0~9의 값

"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"

해당 값을 나타내는 단어가 섞여있는 문자열을 받아 작은 수 부터 차례로 정렬하여 출력

"""
# 버블 정렬
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = input().split()
    arr = list(input().split())
    # 행성숫자 딕셔너리 구성
    planet = {"ZRO":0 , "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
    new_arr = []
    new_arr2 = []
    # 입력받은 배열 순회 하면서, 딕셔너리를 참고해서 해당하는 값을 new_arr에 넣는다
    for i in arr:
        if i in planet:
            new_arr.append(planet[i])
    # new_arr를 버블 정렬로 정렬한다
    bubble_sort(new_arr)

    # 새로 구성한 배열을 순회하면서, 딕셔너리를 참고해서 해당하는 키를 new_arr2에 넣는다
    for i in new_arr:
        for k, v in planet.items():
            if i == v:
                new_arr2.append(k)
    print(f'#{tc}')
    print(*new_arr2)

