
import sys
sys.stdin = open('input.txt')


T= int(input())
for tc in range(1,T+1):
    #정사각형 변의 길이
    N = int(input())
    #비어있는 정사각형
    arr = [[0]*(N) for _ in range(N)]
    #방향 설정
    di = [0,1,0,-1] # 각각 우, 하, 좌, 상
    dj = [1,0,-1,0] #      0   1   2   3
    k = 0
    #숫자 설정
    cnt = 1
    #위치 설정
    ni = 0
    nj = 0
    #배열의 초기값 설정
    arr[ni][nj] = cnt
    while True:
        # 만약, 현재 숫자의 값이 n의 제곱값과 같다면, 반복문을 끝낸다
        if cnt == N ** 2:
            break
        # #현재 위치를 설정한 방향으로 이동해준다
        ni += di[k]
        nj += dj[k]
        #만약, 이동한 위치가 정상적이고, 이동한 배열의 값이 0이라면
        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] == 0:
                #카운트를 1 늘리고 이동한 위치에 숫자를 기입한다
                cnt += 1
                arr[ni][nj] = cnt
                print(arr[ni][nj])
                print(k)
        #만약, 이동한 위치가 이상하거나, 배열의 값이 0이 아니라면
        else:
            #다시 되돌아간다
            #되돌아갔을때 거기도 0이 아니라면, 무한루프가 걸리므로 조건 추가
            ni -= di[k]
            nj -= dj[k]
            #방향 설정 바꿔주고,
            k = (k + 1) % 4
            print('방향 설정', k)
            #다시 반복문 시작한다
            continue
    print(arr)


