from collections import defaultdict
def solution(nums):
    answer = 0
    set_ = set()
    arr = []
    N = len(nums)
    for num in nums:
        set_.add(num) 
    if (len(set_) <= N // 2):
        return len(set_)
    else:
        return N // 2
