# 실습 번호.py
import book

number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age, address):
    
    increase_user()
    user_info = {}
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address
    print(f'{name}님 환영합니다!')
    return user_info


many_user = list(map(create_user, name, age, address))

# def userfunc22(many_user):
#     userdic22 = {} 
#     userdic22['name'] = many_user['name'] 
#     userdic22['age'] = many_user['age']
#     return userdic22
# info = list(map(userfunc22, many_user))

info = list(map(lambda x: {'name' : x['name'], 'age' : x['age']}, many_user))


def rental_book(info):
    book33 = info['age']//10
    book.decrease_book(book33)
    print(f'{info["name"]}님이 {book33}권의 책을 대여하였습니다.')
list(map(rental_book, info))

#fstring을 감싸는 ''와 딕셔너리 변수의 문자열의 ''는 서로 달라야한다
#그냥 함수로 새로운 딕셔너리 할당과 람다 함수의 딕셔너리 할당의 차이는 다음과 같다
#기존 함수는 딕셔너리를 선언한다
#람다 함수는 딕셔너리를 선언하지 않는다
#기존 함수는 새딕셔너리[키] = 인자[키]로 새로운 딕셔너리값을 할당한다
#람다 함수는 {키1 : 인자[키1], 키2 : 인자[키2]}로 새로운 딕셔너리를 할당한다
#두 방식의 차이는 =과 :의 차이이다
#=은 공딕셔너리 생성후 할당하는것이다
#:은 공딕셔너리 생성하지 않고 바로 할당하는 것이다
#람다 함수는 기존 함수에서의 return 값을 바로 lambda x: 뒤에 작성하는 것으로 보인다
#람다 함수는 lambda x: 기존함수의 return, 인자 이다.
