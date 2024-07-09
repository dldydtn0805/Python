import sys
# sys.stdin = open('input.txt')

'''
재료가 n개 있음, 각 재료의 신맛 s 과 쓴맛 b를 알고있다. 여러 재료를 이용해서 요리할때

그 음식의 신맛은 재료들의 신맛의 곱이고, 쓴맛은 합이다

신맛과 쓴맛의 차이를 작게 만들고싶다

재료는 적어도 하나를 사용해야한다


'''
n = int(input())
sours = [0]*n
bitters = [0]*n
for i in range(n):
    sour, bitter = map(int, input().split())
    sours[i] = sour
    bitters[i] = bitter
min_v = 1e9
for i in range(1<<n):
    sum_v = 0
    mul_v = 1
    for j in range(n):
        if i & (1<<j):
            mul_v *= sours[j]
            sum_v += bitters[j]
    if mul_v != 1 and sum_v !=0:
        min_v = min(min_v, (abs(sum_v-mul_v)))
print(min_v)