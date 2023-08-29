n = int(input())
"""
한변을 이루는 점의 갯수
2개 - 3개 - 5개 - 9개 - 17개 - 33개
n2 = n1 + (n1-1) 
"""

cnt = 1
num = 2
while cnt<n+1:
    num = num+(num-1)
    cnt += 1
print(num*num)