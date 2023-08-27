import sys
sys.stdin = open('input.txt')

"""
운영 비용은 K*K+(K-1)*(K-1)

마름모 크기는 정해져있지 않고 K 임

마름모 모양 구하는 for 문으로 마름모 구성하고

ok 틀 만들었음 

구성한 마름모에 해당하는 영역에 집이 있으면 운영비용 합으로 마름모 감당할수있는지 확인하고

마름모 감당할수있으면 집의 개수를 저장하고

저장한 집들의 개수 중에 최대 집 개수를 찾으면 된다


"""
# 마름모 만드는 함수
def marm(x,y,k):
    # 마름모 중앙
    tl[x][y] = 1
    cnt = 1
    # 여기에 마름모 다음 턴을 저장
    temp = []
    # k 번째 크기의 마름모가 생성되도록 한다
    while cnt < k:
        for i in range(n):
            for j in range(n):
                if tl[i][j] == 1:
                    # 사방을 확인하고 다음턴에 저장한다
                    for g in range(4):
                        ni = i + di[g]
                        nj = j + dj[g]
                        if 0<=ni<n and 0<=nj<n:
                            temp.append((ni,nj))
        # 한 턴 끝나면 마름모 영역 채우기
        while temp:
            a, b = temp.pop()
            tl[a][b] = 1
        cnt += 1

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    # 도시에 집이 있는 위치
    citymap = [list(map(int, input().split())) for _ in range(n)]
    di = [-1,0,1,0]
    dj = [0,1,0,-1]
    money = 0
    max_money = 0
    # 도시에 전체 사람들의 명수
    for i in range(n):
        for j in range(n):
            if citymap[i][j] == 1:
                money += 1
    max_cnt = 0
    k = 1
    while True:
        # 도시 전체 사람들의 돈 보다 마름모의 영역이 더 넓다면 중지
        if k*k+(k-1)*(k-1) > money*m:
            break
        # 마름모를 가능한 모든 영역에 만들어보면서 해당 마름모의 영역에 사람들이 얼마나 존재하는지 체크한다
        for i in range(n):
            for j in range(n):
                cnt = 0
                tl = [[0]*n for _ in range(n)]
                marm(i,j,k)
                for a in range(n):
                    for b in range(n):
                        if tl[a][b] == 1 and citymap[a][b] == 1:
                            cnt+=1
                # 만약에 해당 영역의 비용보다 지역 사람들의 돈이 더 많거나 같으면 최대 명수에 넣어준다
                if k*k+(k-1)*(k-1) <= cnt*m:
                    max_cnt = max(cnt, max_cnt)
        k+= 1

    print(f'#{tc}', max_cnt)
