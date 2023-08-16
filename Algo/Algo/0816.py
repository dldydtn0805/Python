"""
def f(i,N):
  if i==N:
    return
  else:
    B[i] = A[i]
    f(i+1, N)

N = 3
A = [1,2,3]
B = [0] * N
f(0, N)
print(B)

재귀
"""
"""
def f(i,N):
    if i == N:
        s = 0 # 합
        for j in range(N):
            if bit[j]:
                s += A[j]
        print(s)
        return
    else:
        bit[i] = 1
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)

A = [1,2,3]
bit = [0]*3
f(0, 3)

부분집합의 합 재귀
"""

"""
def f(i,N, s): #s : i-1 원소까지 부분집합의 합(포함된 원소의 합)
    if i == N:
        print(s)
        return
    else:
        bit[i] = 1 #부분집합에 A[i] 포함
        f(i+1, N, s+A[i])
        bit[i] = 0 #부분집합에 A[i] 빠짐
        f(i+1, N, s)


A = [1,2,3]
bit = [0]*3
f(0, 3, 0)

부분집합의 합 재귀2
"""

"""
# 부분집합의 합

def f(i,N, s): #s : i-1 원소까지 부분집합의 합(포함된 원소의 합)
    if i == N:
        if s == 10:
            print(bit)
        return
    else:
        bit[i] = 1 #부분집합에 A[i] 포함
        f(i+1, N, s+A[i])
        bit[i] = 0 #부분집합에 A[i] 빠짐
        f(i+1, N, s)

# 1부터 10까지 원소인 집합, 부분집합의 합이 10인 경우는?
N = 10
A = [i for i in range(1,N+1)]
bit = [0]*N
f(0, N, 0)
"""


"""
백트래킹 부분집합의 합
def f(i,N, s, t): #s : i-1 원소까지 부분집합의 합(포함된 원소의 합), t 찾고자 하는 합
    global cnt
    cnt += 1
    if s == t: #
        if s == 10:
            return
    elif i == N: # 남은 원소가 없는 경우
        return
    elif s > t:
        return
    else:
        bit[i] = 1 #부분집합에 A[i] 포함
        f(i+1, N, s+A[i], t)

        bit[i] = 0 #부분집합에 A[i] 빠짐
        f(i+1, N, s, t)

# 1부터 10까지 원소인 집합, 부분집합의 합이 10인 경우는?
N = 10
A = [i for i in range(1,N+1)]
bit = [0]*N
cnt = 0
f(0, N, 0, 10)
print(cnt)

"""
"""
def f(i, N):
    if i == N:
        print(A)
    else:
        for j in range(i, N): # 자신부터 오른쪽 끝까지
            A[i], A[j] = A[j], A[i]
            f(i+1, N)
            A[i], A[j] = A[j], A[i]

A = [1,2,3]
f(0,3)

"""
"""

def f(i, N):
    if i == N:
        print(A)
    else:
        for j in range(i, N): # 자신부터 오른쪽 끝까지
            A[i], A[j] = A[j], A[i]
            f(i+1, N)
            A[i], A[j] = A[j], A[i]

A = [0,1,2]
f(0,3)
"""

def f1(b, e):
    global cnt1

    if b == 0:
        return 1
    r = 1
    for i in range(e):
        r *= b
        cnt1+=1
    return r

def f2(b, e):
    global cnt2
    if b == 0 or e == 0:
        return 1
    if e % 2: # 홀수면
        r = f2(b, (e-1)//2)
        cnt2 += 1
        return r*r*b
    else: # 짝수면
        r = f2(b, e//2)
        cnt2 += 1
        return r*r

cnt1 = 0
cnt2 = 0
print(f1(2,20), cnt1)
print(f2(2,20), cnt2)

