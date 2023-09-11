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

#안이 가득 채워져있는지 확인하기


# 꼭지점이 세개일때만 아래를 시행한다
if len(dot) == 3:
    #각 꼭지점간의 거리 구하기
    d1 = math.sqrt(abs(dot[0][0] - dot[1][0])**2 +abs(dot[0][1] - dot[1][1])**2)
    d2 = math.sqrt(abs(dot[1][0] - dot[2][0])**2 +abs(dot[1][1] - dot[2][1])**2)
    d3 = math.sqrt(abs(dot[2][0] - dot[0][0])**2 +abs(dot[2][1] - dot[0][1])**2)

    # 만약 d1과 d2가 같을때
    if d1 == d2:
        compare_v1 = round(d1**2 + d2**2, 2)
        compare_v2 = round(d3**2, 2)
        if compare_v1 == compare_v2:
            for i in dot:
                print(*i)
        else:
            print(0)
    # 만약 d2과 d3가 같을때
    elif d2 == d3:
        compare_v1 = round(d2**2 + d3**2, 2)
        compare_v2 = round(d1**2, 2)
        if compare_v1 == compare_v2:
            for i in dot:
                print(*i)
        else:
            print(0)
    # 만약 d3과 d1가 같을때
    elif d3 == d1:
        compare_v1 = round(d3**2 + d1**2, 2)
        compare_v2 = round(d2**2, 2)
        if compare_v1 == compare_v2:
            for i in dot:
                print(*i)
        else:
            print(0)
    else:
        print(0)
else:
    print(0)

# 삼각형이 비어있는지 확인하는 문구

