# 이미 사용한 숫자는 사용하지 않도록하는 조건을 걸어준다면?

arr = [i for i in range(1,4)]
path = [0] * 3
def backtracking(cnt):
    # 기저조건
    # 숫자 3개를 골랐을때 종료
    if cnt == 3:
        print(*path)
        return
    for num in arr:
        # 백트래킹 할때 핵심, 가지치기 - 중복된 숫자 제거
        # 조건을 어떻게 작성할지가 핵심
        if num in path:
            continue
        # 들어가기 전 로직 - 경로 저장
        path[cnt] = num
        # 다음 재귀함수 호출
        backtracking(cnt + 1)
        # 돌아와서 할 로직
        # 백트래킹 할때 핵심, 초기화
        path[cnt] = 0

backtracking(0)


def func():
    pass
    # 재귀를 끝내는 기저조건

    # 가지치기

    # 반복문
        # 가지치기

        # 재귀 들어가기전

        # 재귀함수 호출

        # 돌아와서