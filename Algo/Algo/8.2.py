# # x = 0
# # y = 1
# # N = 0
# # dx = []
# # dy = []
# # for d in range(4):
# #     #다음에 이동할 좌표 담기
# #     nx = x + dx[d]
# #     ny = y + dy[d]
# #
# #     #map 을 벗어나는 경우 아무것도 하지않기
# #     if nx < 0 or nx >= N or ny < 0 or ny >= N:
# #         continue
# #     print('결과프린트')
# #
# #     #특정 로직 수행
# # def is_safe_area(nx, ny):
# #     if nx <= 0 < N and 0 <= ny < N:
# #         return True
# #     return False
# #
# #     #벽을 넘어가지 않는 경우에만 수행하기
# # if is_safe_area(nx,ny): #탐색 가능한 좌표 확인
# #     pass
# #     #로직 수행
# #
# def print_subset(bit, arr, n):
#   total = 0 #부분집합의 함
#   for i in range(n):
#     if bit[i]:
#       print(arr[i], end = ' ')
#       total += arr[i]
#   print(bit, total)
#
# arr = [1,2,3,4]
# bit = [0,0,0,0]
#
# for i in range(2): #0번 원소
#   bit[0] = i
#   for j in range(2): #1번 원소
#       bit[1] = j
#       for k in range(2): #2번 원소
#           bit[2] = k
#           for l in range(2): #3번 원소
#               bit[3] = l
#               print_subset(bit, arr, 4) #생선된 부분집합

arr = [1,2,3]

n = len(arr) #n 원소의 개수

for i in range(1<<n): # 1<<n 부분집합의 개수
  for j in range(n): #원소의 수 만큼 비트를 비교함
    if i & (1<<j): # i의 j번 비트가 1인 경우
      print(arr[j], end=", ") #j번 원소 출력

  print()
print()