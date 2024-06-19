def recursion(corner_i, corner_j, current_size):
    if current_size == 3:
        arr[corner_i][corner_j] = '*'
        arr[corner_i][corner_j-1] = '*'
        arr[corner_i][corner_j-2] = '*'
        arr[corner_i][corner_j-3] = '*'
        arr[corner_i][corner_j-4] = '*'
        arr[corner_i-1][corner_j-1] = '*'
        arr[corner_i-1][corner_j-3] = '*'
        arr[corner_i-2][corner_j-2] = '*'
    else:
        #top_triangle
        recursion(corner_i - current_size//2, corner_j - current_size//2, current_size//2)
        #left_triangle
        recursion(corner_i, corner_j - current_size, current_size//2)
        #right_triangle
        recursion(corner_i, corner_j, current_size//2)
N = int(input())
arr = [[' ' for _ in range(N*2+1)] for _ in range(N+1)]
recursion(N, 2*N, N)
for i in range(1, len(arr)):
    print(''.join(arr[i])[2:])
