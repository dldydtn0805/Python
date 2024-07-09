import sys, math
input = sys.stdin.readline

tri = [list(input()) for _ in range(10)]
dot = []

# 꼭짓점 찾아내기
for i in range(10):
    for j in range(10):
        if tri[i][j] == '1' and tri[i][j-1] == '0' and tri[i][j+1] =='0':
            dot.append([i+1, j+1])

for i in range(10):
    for j in range(10):
        if tri[j][i] == '1' and tri[j-1][i] == '0' and tri[j+1][i] =='0':
            dot.append([j+1, i+1])

dot.sort()

<<<<<<< HEAD
=======
#안이 가득 채워져있는지 확인하기


>>>>>>> 291b239649747c66346a45492fad13d084304393
# 꼭지점이 세개일때만 아래를 시행한다
if len(dot) == 3:
    #각 꼭지점간의 거리 구하기
    d1 = math.sqrt(abs(dot[0][0] - dot[1][0])**2 +abs(dot[0][1] - dot[1][1])**2)
    d2 = math.sqrt(abs(dot[1][0] - dot[2][0])**2 +abs(dot[1][1] - dot[2][1])**2)
    d3 = math.sqrt(abs(dot[2][0] - dot[0][0])**2 +abs(dot[2][1] - dot[0][1])**2)
<<<<<<< HEAD
    # 만약 d1과 d2가 같을때
    if d1 == d2:
        compare_v1 = round(d1**2 + d2**2, 2)
        compare_v2 = round(d3**2,2)
=======

    # 만약 d1과 d2가 같을때
    if d1 == d2:
        compare_v1 = round(d1**2 + d2**2, 2)
        compare_v2 = round(d3**2, 2)
>>>>>>> 291b239649747c66346a45492fad13d084304393
        if compare_v1 == compare_v2:
            for i in dot:
                print(*i)
        else:
            print(0)
    # 만약 d2과 d3가 같을때
    elif d2 == d3:
        compare_v1 = round(d2**2 + d3**2, 2)
<<<<<<< HEAD
        compare_v2 = round(d1**2,2)
=======
        compare_v2 = round(d1**2, 2)
>>>>>>> 291b239649747c66346a45492fad13d084304393
        if compare_v1 == compare_v2:
            for i in dot:
                print(*i)
        else:
            print(0)
    # 만약 d3과 d1가 같을때
    elif d3 == d1:
        compare_v1 = round(d3**2 + d1**2, 2)
<<<<<<< HEAD
        compare_v2 = round(d2**2,2)
=======
        compare_v2 = round(d2**2, 2)
>>>>>>> 291b239649747c66346a45492fad13d084304393
        if compare_v1 == compare_v2:
            for i in dot:
                print(*i)
        else:
            print(0)
    else:
        print(0)
else:
    print(0)
<<<<<<< HEAD
# # 세 꼭지점을 기준으로 삼각형을 만들고 그 안에 0이 있으면 안되고 그 외에 1이 있으면 안됨
visited = [[0]*10 for _ in range(10)]
if len(dot)==3:
    if dot[0][1] < dot[1][1]:
        x = dot[0][0]
        y = dot[0][1]
        visited[x][y] = 1
        while x < dot[1][0] and y < dot[1][1]:
            x += 1
            y += 1
            visited[x][y] = 1
            if tri[x][y] != 1:
                flag = 0
        while y < dot[1][1]:
            x = dot[0][0]
            y += 1
            visited[x][y] = 1
            if tri[x][y] != 1:
                flag = 0
    elif dot[0][1] > dot[1][1]:
        x = dot[0][0]
        y = dot[0][1]
        visited[x][y] = 1
        while x < dot[1][0] and y > dot[1][1]:
            x += 1
            y -= 1
            visited[x][y] = 1
            if tri[x][y] != 1:
                flag = 0
        while y > dot[1][1]:
            y -= 1
            visited[x][y] = 1
            if tri[x][y] != 1:
                flag = 0
    if dot[1][1] < dot[2][1]:
        x = dot[1][0]
        y = dot[1][1]
        visited[x][y] = 1
        while x < dot[2][0] and y < dot[2][1]:
            x += 1
            y += 1
            visited[x][y] = 1
            if tri[x][y] != 1:
                flag = 0
        while y < dot[2][1]:
            y += 1
            visited[x][y] = 1
            if tri[x][y] != 1:
                flag = 0
    elif dot[1][1] > dot[2][1]:
        x = dot[1][0]
        y = dot[1][1]
        visited[x][y] = 1
        while x < dot[2][0] and y > dot[2][1]:
            x += 1
            y -= 1
            visited[x][y] = 1
            if tri[x][y] != 1:
                flag = 0
        while y > dot[2][1]:
            y -= 1
            visited[x][y] = 1
            if tri[x][y] != 1:
                flag = 0

    if dot[2][1] < dot[0][1]:
        x = dot[2][0]
        y = dot[2][1]
        visited[x][y] = 1
        while x < dot[0][0] and y < dot[0][1]:
            x += 1
            y += 1
            visited[x][y] = 1
            if tri[x][y] != 1:
                flag = 0
        while y < dot[0][1]:
            y += 1
            visited[x][y] = 1
            if tri[x][y] != 1:
                flag = 0
    elif dot[2][1] > dot[0][1]:
        x = dot[2][0]
        y = dot[2][1]
        visited[x][y] = 1
        while x < dot[0][0] and y > dot[0][1]:
            x += 1
            y -= 1
            visited[x][y] = 1
            if tri[x][y] != 1:
                flag = 0
        while y > dot[0][1]:
            x = dot[2][0]
            y -= 1
            visited[x][y] = 1
            if tri[x][y] != 1:
                flag = 0
print(visited)
=======

# 삼각형이 비어있는지 확인하는 문구

>>>>>>> 291b239649747c66346a45492fad13d084304393
