from collections import deque

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def get_string(puzzle):
    return ''.join(str(num) for row in puzzle for num in row)

def get_array(state):
    return [[int(state[i * 3 + j]) for j in range(3)] for i in range(3)]

def bfs(puzzle):
    initial_state = get_string(puzzle)
    target_state = "123456780"
    
    if initial_state == target_state:
        return 0
    
    queue = deque([(initial_state, 0)])  # (퍼즐 상태, 이동 횟수)
    visited = {initial_state}
    
    while queue:
        state, depth = queue.popleft()
        grid = get_array(state)
        
        # 0(빈칸)의 위치 찾기
        ci, cj = [(i, j) for i in range(3) for j in range(3) if grid[i][j] == 0][0]
        
        for di, dj in directions:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < 3 and 0 <= nj < 3:
                next_grid = [row[:] for row in grid]
                next_grid[ci][cj], next_grid[ni][nj] = next_grid[ni][nj], next_grid[ci][cj]
                next_state = get_string(next_grid)
                
                if next_state == target_state:
                    return depth + 1
                
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, depth + 1))
    
    return -1

# 입력 받기
puzzle = [list(map(int, input().split())) for _ in range(3)]
print(bfs(puzzle))
