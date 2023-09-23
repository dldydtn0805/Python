n = int(input())

"""
거리 1인 방들 = 2~7 = 6개
거리 2인 방들 = 8~19 = 12개 
거리 3인 방들 = 20~37 = 18개
거리 4인 방들 = 38~61 = 24개 아닐까ㅏ
최소 거리는?
"""

a = 0
b = 1
cnt = 1
while True:
    a = b + 1
    b = b + 6*cnt
    cnt += 1
    if a < n <= b:
        break

print(cnt)
