list_of_book = ['장화홍련전','가락국 신화','온달 설화','금오신화','이생규장전','만복자서포기','수성지','백호집','원생몽유록','홍길동전','장생전','도문대작','옥루몽','옥련몽']

rental_book = ['장생전','위대한 개츠비', '원생몽유록','이생규장전', '데미안', '장화홍련전','수성지','백호집','난중일기','홍길동전','만복자서포기']

missing_book = []

check = True

# for book22 in rental_book:
#     if book22 not in list_of_book:
#         missing_book.append(book22) 
#         check = False

missing_book = [i for i in rental_book if i not in list_of_book]

if len(missing_book) > 0:
    check = False

if check is True:
    print('모든 도서가 대여 가능한 상태입니다.')

elif check is False:
    for book33 in missing_book:
        print(f'{book33}을 보충하여야합니다.')

#리스트 컴프리헨션 [i for i in X if i not in Y]으로 리스트를 생성한다
#X에 있는 요소 중 Y에 없는 것들로 리스트를 구성한다는 의미이다
