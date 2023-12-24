
import sys
sys.stdin = open('input.txt')


T= int(input())
for tc in range(1,T+1):
    # 정사각형 변의 길이 입력 받기
    N = int(input())
    # 비어있는 정사각형 설정하기
    arr = [[0]*(N) for _ in range(N)]
    # 오른쪽 -> 아래 -> 왼쪽 -> 위쪽 순으로 방향 세우기
    di = [0,1,0,-1] # 각각 우, 하, 좌, 상
    dj = [1,0,-1,0] #      0   1   2   3
    #방향 전환하는 변수 설정
    k = 0
    #숫자 설정
    cnt = 1
    #위치 설정
    ni = 0
    nj = 0
    # 배열의 초기값 설정하기
    arr[0][0] = cnt
    # 만약, 현재 숫자의 값이 n의 제곱값보다 커진다면, 반복문을 끝낸다
    while cnt < N**2:
        #현재 위치를 설정한 방향으로 이동해준다
        ni += di[k]
        nj += dj[k]
        #만약, 이동한 위치가 정상적이고, 이동한 배열의 값이 0이라면
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            #카운트를 1 늘리고 이동한 위치에 숫자를 기입한다
            cnt += 1
            arr[ni][nj] = cnt

        #만약, 이동한 위치가 이상하거나, 배열의 값이 0이 아니라면
        else:
            #한칸 다시 되돌아간다
            ni -= di[k]
            nj -= dj[k]
            # 방향 전환 변수인 k에 1을 더해서 다음 순서 방향으로 넘긴다
            # 방향 설정 인덱스가 4개 뿐이라서, 4로 나눈 나머지의 개수를 할당하면 된다
            k = (k + 1) % 4
            continue
    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])


