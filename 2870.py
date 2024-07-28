import sys
input = sys.stdin.readline

N = int(input())
ans = []
for _ in range(N):
    res = list(input().rstrip())
    tmp = ''
    for i in range(len(res)):
        if tmp == '':
            if res[i].isnumeric():
                tmp += res[i]
        else:
            if res[i].isnumeric():
                tmp += res[i]
            else:
                ans.append(int(tmp))
                tmp = ''
    if tmp != '':
        ans.append(int(tmp))
answers = (sorted(ans))
for answer in answers:
    print(answer)
