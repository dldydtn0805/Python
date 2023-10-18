import sys
# sys.stdin = open('input.txt')

arr = []
for _ in range(5):
    arr.append(int(input()))

arr.sort()
print(f'{sum(arr)/len(arr):.0f}')
print(arr[2])