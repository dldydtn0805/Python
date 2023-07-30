# ws_3_3.py
import book
def rental_book(name11, book22):
    book.decrease_book(book22)
    print(f'{name11}님이 {book22}권의 책을 대여하였습니다.')

rental_book('홍길동', 3)

#모듈 불러올때, import 모듈이름.py가 아니라 import 모듈이름 이다.
