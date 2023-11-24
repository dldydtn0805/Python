N = int(input())

arr = []

for _ in range(N):
    start, end = input().split()
    print('시작:',  int(start[0:2])*60 + int(start[2:]))
    print('끝:', int(end[0:2]) * 60 + int(end[2:]))
    s = int(start[0:2])*60 + int(start[2:])
    e = int(end[0:2]) * 60 + int(end[2:])

    if not arr:
        arr.append((s,e))

    flag = 0

    for i in range(len(arr)):
        if arr[i][0] <= s <= arr[i][1]:
            if e > arr[i][1]:
                arr[i] = (arr[i][0], e)
                flag = 1
        elif arr[i][0] <= e <= arr[i][1]:
            if s < arr[i][0]:
                arr[i] = (s, arr[i][1])
                flag = 1

    if not flag:
        arr.append((s,e))

print(set(arr))

운행 + 쉬는 = 720

운행 = 550


놀이기구 운행 전 + 운행 중간중간 비는 텀 + 놀이기구 다 ~ 끝나고 쉬는시간 = 170
20  + 110 +40  = 170

380

130  510 40 550