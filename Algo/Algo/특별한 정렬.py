"""
N개의 정수가 주어지면 가장 큰수, 가장 작은수, 2번째 큰수, 2번째 작은수로 번갈아 정렬한다

주어진 숫자에 대해 특별한 정렬을 10개까지 수행한다

입력

정수 N개가 주어지고, 다음줄에 N개의 정수들이 주어진다

단, 10<=N<=100

1<=정수<=100 이다
"""

#정방향 버블 정렬
def sort_arr(x):
    #i는 배열 끝에서 배열 처음까지 순회한다
    for i in range(len(x)-1, 0, -1):
        #j는 배열 처음 부터 위의 i 만큼까지 순회한다
        for j in range(i):
            # j보다 j+1가 **크다면
            if x[j] > x[j+1]:
                #j와 j+1의 위치를 바꾼다
                x[j], x[j+1] = x[j+1], x[j]

    return x

#역방향 버블 정렬
def reverse_arr(x):
    #i는 배열 끝에서 배열 처음까지 순회한다
    for i in range(len(x)-1, 0, -1):
        #j는 배열 처음 부터 위의 i 만큼까지 순회한다
        for j in range(i):
            # j보다 j+1가 **작다면
            if x[j] < x[j+1]:
                #j와 j+1의 위치를 바꾼다
                x[j], x[j+1] = x[j+1], x[j]

    return x


import sys
sys.stdin = open('input.txt')

T= int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    sort_arr(arr)
    #정방향 배열
    true_arr = arr[:]
    #역방향 배열
    reversed_arr = reverse_arr(arr)
    #비어있는 리스트 여유를 두고 생성
    new_arr = [0]*10

    i = 0
    #짝수 열에 역방향 배열 삽입
    while True:
        new_arr[2*i] = reversed_arr[i]
        i+=1
        if i == 5:
            break
    #홀수 열에 정방향 배열 삽입
    i = 0
    while True:
        new_arr[2*i+1] = true_arr[i]
        i+=1
        if i == 5:
            break
    print(f'#{tc}', *new_arr)