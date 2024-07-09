A = [1,2,3,4,5,6,7]
r = 3
n = 7
comb = [0]*r
perm = [0]*r

def nPr(n,r,cnt):
    if cnt==r:
        print(*perm)
        return
    else:
        for i in range(n):
            if A[i] in perm:
                continue
            perm[cnt] = A[i]
            nPr(n, r, cnt+1)
            perm[cnt] = 0

def nCr(n,r,s):
    if r == 0:
        print(*comb)
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr(n,r-1,i+1)

def subSet():
    for i in range(1<<n):
        for j in range(n):
            if i & (1<<j):
                print(A[j], end=' ')
        print()

# nPr(n,r,0)
# nCr(n,r,0)
# subSet()

arr = [2,4,5,6,7,8,8]
arr.sort()
def binarySearch(target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return '해당 데이터는 없습니다'

def binarySearch2(low, high, target):
    if low > high:
        return - 1
    mid = (low + high) // 2
    if target == arr[mid]:
        return mid
    elif arr[mid] < target:
        return binarySearch2(mid+1, high, target)
    else:
        return binarySearch2(low, mid-1, target)

print(binarySearch(8))
print(binarySearch2(0, len(arr)-1, 5))
