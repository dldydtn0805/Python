# main.py

# 아래 함수를 수정하시오.
def find_min_max(aaa):
    aaa.sort()
    bbb = aaa[0], aaa[-1]
    return bbb
result = find_min_max([3, 1, 7, 2, 5])
print(result) # (1, 7)

#리스트를 sort로 정렬한다