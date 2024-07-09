import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# 순서대로 전위 중위 후위 순회이다 chr와 ord를 사용해서 알파벳과 숫자를 치환했다
def pre(k):
    global preo
    if k:
        preo += (chr(ord('A')+k-1))
        pre(r1[k])
        pre(r2[k])
def mid(k):
    global mido
    if k:
        mid(r1[k])
        mido += (chr(ord('A')+k-1))
        mid(r2[k])
def post(k):
    global poso
    if k:
        post(r1[k])
        post(r2[k])
        poso += (chr(ord('A')+k-1))
n = int(input())
r1 = [0]*(n+1)
r2 = [0]*(n+1)
# 각각 순회 결과값
preo = ''
mido = ''
poso = ''
# 입력 받으면서 왼쪽 자식 노드 오른쪽 자식노드를 ord를 사용해서 작성해주었다 노드 좌표는 1부터 시작하기 때문에 각각에 1을 더해주었다
for _ in range(n):
    a, b, c = input().split()
    if b != '.':
        r1[ord(a)-ord('A')+1] = (ord(b)-ord('A')+1)
    else:
        r1[ord(a)-ord('A')+1] = 0
    if c != '.':
        r2[ord(a)-ord('A')+1] = (ord(c)-ord('A')+1)
    else:
        r2[ord(a) - ord('A')+1] = 0

# 문제에서 루트 노드가 A라고 했기 때문에 1로 순회해주었다
pre(1)
print(preo)

mid(1)
print(mido)

post(1)
print(poso)