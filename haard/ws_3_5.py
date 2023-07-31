# 실습 번호.py
import book

number_of_people = 0

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

def increase_user():
    global number_of_people
    number_of_people += 1

def create_user(name, age, address):
    increase_user()
    user_info = {
        'name':name, 
        'age':age, 
        'address':address
    }
    print(f'{name}님 환영합니다!')
    return user_info #이게 중요함
#유저 목록
user_list = list(map(create_user, name, age, address))
# print(user_list)

#address를 어떻게 빼지? 어떻게 제외시키지? 라는 착각에 빠짐 > 사실 무시해도 됨
def make_new_user_list(user_info):
    result = {
        'name': user_info['name'],
        'age': user_info['age']//10,        
    }
    return result

new_user_list = list(map(make_new_user_list, user_list))
# print(new_user_list)

#렌탈이 진행되는 함수
def rental_book(user_info):
    #남은 책 수
    book.decrease_book(user_info['age'])
    print(f'{user_info["name"]}님이 {user_info["age"]}권을 대여했습니다.')

(list(map(rental_book, new_user_list)))