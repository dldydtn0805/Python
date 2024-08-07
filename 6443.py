import sys
input = sys.stdin.readline
from collections import defaultdict

def get_anagram(res):
    if len(res) == M:
        print(res)
        return
    else:
        for i in range(M):
            if not visited[i] and not check[res+alphabets[i]]:
                check[res] = 1
                visited[i] = 1
                get_anagram(res+alphabets[i])
                visited[i] = 0

N = int(input())
for _ in range(N):
    alphabets = list(input().rstrip())
    alphabets.sort()
    visited = [0 for _ in range(len(alphabets))]
    M = len(alphabets)
    check = defaultdict(int)
    for i in range(M):
        if not visited[i]:
            check[alphabets[i]] = 1
            visited[i] = 1
            get_anagram(alphabets[i])
            visited[i] = 0
exit()

