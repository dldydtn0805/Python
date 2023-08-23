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
c1 = [] * 1000
c2 = [] * 1000
middle = value[0]
value.sort()
middle = value.index(middle)
left = value[:5]
right = value[6:]
print(left)
print(right)