import sys
input = sys.stdin.readline
import math

# 소수판별
def judge(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

a = []

for i in range(123457*2):
    if judge(i) == True:
        a.append(i)


for i in range(123457):
    N = int(input())
    if N == 0:
        break
    cnt = 0
    for j in range(len(a)):

        if a[j] > N:
            cnt += 1

        if a[j] > 2 * N:
            break
    print(cnt-1)

is_prime = [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0]
sum = [0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4]
# sum[i] = is_prime[0]~is_prime[i]
#isp[3]~isp[6] = (isp[0]~isp[6])-(isp[0]~isp[2]) = sum[6]-sum[2]
#
#
#
#
# for i in range(123457):
#     N = int(input())
#     for j in range(len(a)):
#         if N == 0:
#             break
#         cnt = 0
#         if a[j] > N:
#             cnt += 1
#             if a[j] > 2*N+1:
#                 continue
#         print(cnt)
#











