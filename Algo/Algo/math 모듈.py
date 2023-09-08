import math

start = (1,1)
end = (2,2)

# x좌표의 차이
a = abs(end[0] - start[0])
# y좌표의 차이
b = abs(end[1] - start[1])

r = math.sqrt(a**2+b**2)
# 아크탄젠트는 math.atan 함수를 이용하면 계산할수있음
# math.atan의 결과는 radian으로 나옴(degree가 아님)
radian = math.atan(b/a)

print(r, math.degrees(radian))
