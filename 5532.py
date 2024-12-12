L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
if A%C:
    Q = A//C+1
else:
    Q = A//C
if B%D:
    W = B//D+1
else:
    W = B//D
X = max(Q, W)
print(L-X)