"""
한쪽 벽면에 다음과 같이 노란색 상자들이 쌓여있다

높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업을 평탄화라고 한다

평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다

평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려있을때, 제한된 횟수만큼 옮기는 작업을 한 후,

최고점과 최저점의 차이를 반환하는 프로그램을 작성하시오

제약 사항

가로의 길이는 항상 100이다

모든 위치에서 상자의 높이는 1이상 100 이하이다

덤프 횟수는 1이상 1000이하이다

덤프 횟수 이내에 평탄화가 완료되면, 더이상 덤프를 수행할 수 없으므로 그때의 최고점과 최저점 높이 차를 반환한다 데이터에 따라 1 or 0이 된다

"""
# 평탄화 재귀 함수 작성
# 재귀 맞나???
def flatten(arr, cnt):
    # 최고 높이, 최저 높이 설정
    min_h = 100
    max_h = 1

    for i in range(100):
        # 최저 높이 발견했을 때
        if arr[i] < min_h:
            min_h = arr[i]
            # 최저 높이 인덱스 설정
            min_hindex = i

        # 최고 높이 발견 했을 때
        if arr[i] > max_h:
            max_h = arr[i]
            # 최고 높이 인덱스 설정
            max_hindex = i

    # 재귀 탈출 조건. 평탄화가 모두 진행됐을 때의 행동
    # 만약, 평탄화 작업을 모두 진행하기 전에 최고높이와 최저높이의 차이가 1이하라면
    if arr[max_hindex] - arr[min_hindex] <= 1 :
        return arr[max_hindex] - arr[min_hindex]
    # 만약, 평탄화 작업을 모두 진행했다면,
    if cnt == 0:
        return arr[max_hindex] - arr[min_hindex]


    # 평탄화 작업 실시하기
    arr[min_hindex] += 1
    arr[max_hindex] -= 1
    cnt -= 1

    return flatten(arr, cnt)

import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    # cnt 평탄화 작업 실시 횟수
    cnt = int(input())
    arr = list(map(int,input().split()))
    result = flatten(arr, cnt)
    print(f'#{tc}', result)