import sys
input = sys.stdin.readline

S, E, Q = input().split()
check = set()
ans = 0
while True:
    try:
        time, name = input().split()
        if time <= S:
            if name not in check:
                check.add(name)
        elif E <= time <= Q:
            if name in check:
                ans += 1
                check.remove(name)
    except:
        break
print(ans)
