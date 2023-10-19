import sys
# sys.stdin = open('input.txt')

input = sys.stdin.readline

a, b =  map(int, input().rstrip().split())

arr1 = set(list(map(int, input().rstrip().split())))

arr2 = set(list(map(int, input().rstrip().split())))

print(len(arr1 ^ arr2))