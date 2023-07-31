# 실습 번호.py

number_of_book = 100

def decrease_book(new_dict):
    global number_of_book 
    number_of_book -= new_dict['age']//10
    return number_of_book

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

 
def create_user(name, age, address):
    dict = {'name':name, 'age':age, 'address':address}
    print(f'{name}님 환영합니다!')
    return dict


many_user = list(map(create_user, name, age, address))

# def new_dict(many_user):
#     new_dict = {'name':many_user['name'], 'age':many_user['age']}
#     return new_dict

# 위의 식을 lambda 함수 표현식으로 하면? 아래와 같다 
new_dict = list(map(lambda x : {'name':x['name'], 'age':x['age']}, many_user))

def rental_book(new_dict):
    print('남은 책의 수 : ', decrease_book(new_dict))
    print(f'{new_dict["name"]}님이 {new_dict["age"]//10}권의 책을 대여하였습니다.')

result = map(rental_book, new_dict)
list(result)


# 깨달은 것
# 딕셔너리에서 키를 가지고 값을 찾을때, 딕셔너리['키값'] 으로 찾아야하는데 딕셔너리('키값') 으로 찾고있어서 오류가 발생했다
# map(함수, 반복가능한객체) 이므로 리스트도 들어갈 수 있다, 리스트 안에 뭐가 들어가든 상관 없다 이 문제에서는 딕셔너리가 여러개 들어가있었다
# map, lambda 함수식을 표현할때 어렵게 생각하지말고, (lambda x : 뒤에있는 객체를 대상으로 한 표현식인데 그 객체를 x로 표현한 식, 대상이 되는 객체) 라고 생각하면 쉽다