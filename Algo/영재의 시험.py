import sys
# sys.stdin = open('input.txt')

def dfs(cnt, word):
    global result, r
    if len(word)>2 and word[len(word)-3] == word[len(word)-1] == word[len(word)-2]:
        return
    if cnt == 10:
        value = 0
        for i in range(10):
            if word[i] == r[i]:
                value += 1
        if value >= 5:
            result += 1
        return
    for i in range(5):
        dfs(cnt+1, word+str(ans[i]))


arr = list(input().split())
r = ''.join(arr)
ans = [i for i in range(1,6)]
result = 0
dfs(0,'')

print(result)