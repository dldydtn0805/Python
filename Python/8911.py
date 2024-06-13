import sys
input = sys.stdin.readline

T = int(input())
turtle_head_direction = [
    [1,0], #북
    [0,1], #동
    [-1,0], #남
    [0,-1] #서
]


for tc in range(T):
    max_north = 0
    max_south = 0
    max_east = 0
    max_west = 0
    current_i = 0
    current_j = 0
    current_direction = 0
    command = list(input().rstrip())
    for c in command:
        if c == 'F':
            current_i += turtle_head_direction[current_direction][0]
            current_j += turtle_head_direction[current_direction][1]
        if c == 'B':
            current_i -= turtle_head_direction[current_direction][0]
            current_j -= turtle_head_direction[current_direction][1]
        if c == 'R':
            current_direction = ( current_direction + 1 ) % 4
        if c == 'L':
            if current_direction - 1 < 0:
                current_direction = 3
            else:
                current_direction = ( current_direction - 1 )
        max_north = max(current_i, max_north)
        max_south = min(current_i, max_south)
        max_east = max(current_j, max_east)
        max_west = min(current_j, max_west)
    print((max_north - max_south)*(max_east-max_west))
