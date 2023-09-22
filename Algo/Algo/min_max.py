T = int(input())
for i in range(T):
    N = int(input())
    arr22 = list(map(int, input().split()))
    min22 = arr22[0]
    max22 = arr22[0]

    for j in range(1, N):
        if min22 > arr22[j]:
            min22 = arr22[j]
        if max22 < arr22[j]:
            max22 = arr22[j]
    result = max22 - min22
    print(f'#{i+1} {result}')
