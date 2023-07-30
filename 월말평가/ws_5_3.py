# ws_5_3.py

# 아래 함수를 수정하시오.
def sort_tuple(bbb):
  a, b, c, d, e = bbb
  list33 = [a, b, c, d ,e]
  list33.sort()
  new_tuple = tuple(list33)
  return new_tuple

result = sort_tuple((5, 2, 8, 1, 3))
print(result)

#튜플 인자를 a, b, c, d, e에 언패킹한다
#요소들을 list33에 넣는다
#list33을 sort()로 정렬한다
#list33을 tuple()로 튜플로 만든다
