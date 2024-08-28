import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def backtracking(number):
    string = str(number)
    for i in range(len(string)//2+1):
        if string[i] != string[len(string)-1-i]:
            backtracking(number+10**i)
    else:
        print(number)
        exit()


N = int(input())
backtracking(N+1)
