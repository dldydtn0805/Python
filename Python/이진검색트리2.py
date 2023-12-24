import sys
sys.stdin = open('input.txt')

def preorder(n):
    if n:
        temp.append(n)
        preorder(c1[n])
        preorder(c2[n])

value = []

while True:
    try:
        n = int(input())
        value.append(n)
    except:
        break

temp = []
vl = len(value)
c1 = [0] * len(value)
c2 = [0] * len(value)
middle = value[0]
min_v = min(value)
max_v = max(value)
minturn = value.index(min_v)
maxturn = value.index(max_v)

# 루트 노드 찾기
root = []
for i in range(len(value)):
    if 0 < i <= minturn:
        root.insert(0, value[i])
    elif i <= maxturn and value[0] < value[i]:
        root.append(value[i])

print(root)