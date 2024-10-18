from collections import defaultdict
def solution(phone_book):
    answer = True
    sets_ = set()
    phone_book_ = sorted(phone_book, reverse=True)
    for ele in phone_book_:
        if ele in sets_:
            return False
        for i in range(len(ele)):
            sets_.add(ele[:i+1])
    return True
