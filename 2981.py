import sys
input = sys.stdin.readline
from math import gcd, sqrt

N = int(input())
papers = []
diff = []
for _ in range(N):
    paper = int(input())
    papers.append(paper)

papers.sort()
for i in range(N-1):
    for j in range(i+1, N):
        diff.append(papers[j] - papers[i])

diff = list(set(diff))

if N == 2:
    ans = set()
    ans.add(diff[0])
    for i in range(2, int(sqrt(diff[0])) + 1):
        if not diff[0] % i:
            ans.add(i)
            ans.add(diff[0]//i)
    print(*sorted(list(ans)))

else :
    calc = gcd(diff[0], diff[1])
    for i in range(2, len(diff)):
        calc = gcd(calc, diff[i])

    ans = set()
    ans.add(calc)
    for i in range(2, int(sqrt(calc))+1):
        if not calc % i:
            ans.add(i)
            ans.add(calc//i)

    print(*sorted(list(ans)))

