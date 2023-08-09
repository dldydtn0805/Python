import sys
sys.stdin = open('input.txt')

n = int(input())
words = [input() for _ in range(n)]
# 기준 단어
main = words[0]
ans = 0
cnt = 0
for word in words[1:]:
    if len(word) > len(main)+1:
        cnt += 1
        continue
    for element in main:
       if element in word:
           x = word.replace(element, '')
           word = x
    if len(word)>1:
        cnt += 1
print(n-1-cnt)