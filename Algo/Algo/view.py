for tc in range(10):
    n = int(input())
    arr = list(map(int, input().split()))
    result = 0


    for i in range(2, n-2):
        tmp = arr[i]
        for j in range(i-2, i+3):
            if i==j:
                continue
            if arr[j] < arr[i] and tmp > arr[i] - arr[j]:
                tmp = arr[i] - arr[j]
            elif arr[i] <= arr[j]:
                break
            else:
                result += tmp
    print(result)
