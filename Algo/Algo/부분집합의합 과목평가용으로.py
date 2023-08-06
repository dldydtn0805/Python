
def simple_partsum(arr, bit):
    total = 0
    # **n = len(arr)
    n = len(arr)
    for i in range(n):
        # **if bit[i]:
        if bit[i]:
            print(arr[i], end=' ')
            total += arr[i]
    print(bit, total)



arr = [4,1,2,3]
bit = [0,0,0,0]
for i in range(2):
    # **bit[0] = i
    bit[0] = i
    for j in range(2):
        # **bit[1] = j
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                simple_partsum(arr, bit)

# 비트 연산자 사용해서 부분집합의 합 구하기

arr = [1,2,3,4]
n = len(arr)
for i in range(1<<n):
    total = 0
    # total 은 여기에 들어가야한다
    for j in range(n):
        if i & (1<<j):
            # **arr[j]라는 사실
            print(arr[j], end=' ')
            total += arr[j]
    print()
    print('부분집합의 합', total)