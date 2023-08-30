"""
def f(i,N, key, A): # i 는 현재 상태, N은 목표. key 찾고자 하는 원소
    if i == N:
        return 0 # key가 없는 경우
    elif A[i] == key:
        return 1
    else:
        return f(i+1, N, key, A)

N = 5
A = [1,2,3,4,5]
key = 10
B = [0]*N
print(f(0, N, key, A))
"""

"""
def f(i, N):
    if i == N: # 순열 완성
        print(p)
        return
    else: #p[i]에 들어갈 숫자를 결정
        for j in range(N):
            if used[j] == 0: # 아직 사용 되기 전이면
                p[i] = card[j]
                used[j] = 1
                f(i+1, N)
                used[j] = 0

card = list(map(int, input()))
used = [0] * 6 # 이미 사용한 카드인지 표시
p = [0]*6
f(0,6)

"""
"""
def f(i, N, K): # i는 이전에 고른 개수, N개에서 K개를 고르는 순열
    global cnt
    if i == K: # 순열 완성 K 개를 모두 고른 경우
        cnt += 1
        print(cnt, p)
        return
    else: #p[i]에 들어갈 숫자를 결정
        for j in range(N):
            if used[j] == 0: # 아직 사용 되기 전이면
                p[i] = card[j]
                used[j] = 1
                f(i+1, N, K)
                used[j] = 0

N = 5 # N 개의 숫자에서
K = 5 # K 개를 골라 만드는 순열
card = [1,2,3, 4 ,5]
used = [0] * N # 이미 사용한 카드인지 표시
p = [0]*5
cnt = 0
f(0,N,K)
"""

"""
X = [1,2,3,4,5]
n = 5
a = range(0, (1<<n))
# print(a)

for i in range(0, 2**n):
    temp = ''
    for j in range(n):
        if i & 2**j:
            temp += str(X[j])
    print(temp)

"""

a = [1,2,3,4]
N = 4
# for i in range(1, (1<<N)-1): #맨 첫번째, 마지막 숫자 빼고
for i in range(1, (1<<N)//2): # 절반만 해서 중복 제외 (1<<N) // 2 == 1<<(N-1)
    group1 = []
    group2 = []
    total1 = 0
    total2 = 0
    for j in range(N):
        if i&(1<<j): #j번 비트가 0이 아니면
            group1.append(a[j])
            total1 += a[j]
        else:
            group2.append(a[j])
            total2 += a[j]
    r1 = f(group1)
    r2 = f(group2)
    if r1 and r2:
        if min_v > abs(total1-total2):
    print(group1, group2)
