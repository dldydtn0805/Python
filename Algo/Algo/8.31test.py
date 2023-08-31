


def ncr(n,r):
    if r==0:
        print(tr)
    elif n<r: # 남은 원소보다 고를게 더 많은 원소를 선택해야하는 경우
        return
    else:
        tr[r-1] = a[n-1] # a[n-1] 조합에 포함시키는 경우
        ncr(n-1, r-1)
        ncr(n-1, r) # a[n-1]을 포함시키지 않는 경우

a = [1,2,3,4,5]
R = 3
tr = [0]*R
N = 5
ncr(N,R)

"""
def nCr(n,r,s): #n개에서 r개를 고르는 조합, s 선택할 수 있는 구간의 시작
    if r==0:
        print(*comb)
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr(n,r-1,i+1)
A = [1,2,3,4,5]
N = len(A)
R = 3
comb = [0]*R
nCr(N,R,0)
"""
"""
def subset(i, N):
    if i ==N:
        s= 0
        for j in range(N):
            if bit[j]:
                s+= arr[j]
        if s==0:
            for j in range(N):
                if bit[j]:
                    print(arr[j], end = ' ')
            print()
        return
    else:
        bit[i] = 1
        subset(i+1, N)
        bit[i] = 0
        subset(i+1, N)
    return

arr = [-1,3,-9,6,7,-6,1,5,4,-2]
N = len(arr)
bit = [0]*N
subset(0,N)
"""
"""
def subset(i, N, s,c):
    if s ==0 and c!=0:
        return 1
    elif i == N:
        return 0
    else:
        if subset(i+1, N, s+arr[i], c+1):
            return 1
        if subset(i+1, N, s, c):
            return 1
        return 0

arr = [-1,3,-9,6,7,-6,1,5,4,-2]
N = len(arr)
bit = [0]*N
cnt = 0
print(subset(0,N, 0, 0))
"""
# N = 10
# a = [1,4,1,6,6,10,5,7,3,8,5,9,3,5,8,11,2,13,12,14]
#
# meet = []
# for i in range(N):
#     meet.append([a[i*2],a[i*2+1]])
# meet.sort(key=lambda x:x[1])
# meet = [[0,0]] + meet
# print(meet)
# S = []
# j = 0
# for i in range(1,N+1):
#     if meet[i][0] >= meet[j][1]:#si >= fj
#         S.append(i)
#         j = i
# print(S)