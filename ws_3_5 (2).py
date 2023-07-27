# 실습 번호.py

number_of_book = 100

def decrease_book(number):
    global number_of_book 
    number_of_book -= number
    return number_of_book

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

 
def create_user(name, age, address):
    dict = {'name':name, 'age':age, 'address':address}
    print(f'{name}님 환영합니다!')
    return dict


many_user = list(map(create_user, name, age, address))

print(many_user)

def new_dict(many_user):
    dict = {}
    dict('name') = many_user('name')
    dict('age') = many_user('age')
    pass
    
temp = map(lambda x, y: {'name': x, 'age': y}, many_user)
print(list(temp))
# def rental_book(info):
#     print('남은 책의 수 : ', decrease_book(temp(y))
#     print(f'{temp(x)}님이 {temp(y)}권의 책을 대여하였습니다.')

# map(rental_book, temp)