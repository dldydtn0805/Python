import sys
input = sys.stdin.readline

def cal(dir, pos):
    if dir == 1:
        return pos
    elif dir == 4:
        return W + pos
    elif dir == 2:
        return W + H + (W - pos)
    elif dir == 3:
        return W + H + W + (H - pos)

W, H = map(int,input().split())
N = int(input())
stores = []
for _ in range(N):
    x, y = map(int, input().split())
    stores.append(cal(x,y))
cur_x, cur_y = map(int, input().split())
user = cal(cur_x, cur_y)
ans = 0
for store in stores:
    value = abs(user-store)
    opposite = 2*(W+H)-value
    ans += min(value, opposite)
print(ans)
