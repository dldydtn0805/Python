x = 0
y = 1
N = 0
dx = []
dy = []
for d in range(4):
    #다음에 이동할 좌표 담기
    nx = x + dx[d]
    ny = y + dy[d]

    #map 을 벗어나는 경우 아무것도 하지않기
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        continue
    print('결과프린트')

    #특정 로직 수행
def is_safe_area(nx, ny):
    if nx <= 0 < N and 0 <= ny < N:
        return True
    return False

    #벽을 넘어가지 않는 경우에만 수행하기
if is_safe_area(nx,ny): #탐색 가능한 좌표 확인
    pass
    #로직 수행

