from collections import defaultdict
from math import comb
def solution(clothes):
    answer = 0
    dict = defaultdict(list)
    for name, category in clothes:
        dict[category].append(name)
    ans = 1
    for value in dict.values():
        ans*=len(value)+1 
    
    return ans - 1
