black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']


def create_user(dummy_data):
    censored_user_list = {}
    for data in dummy_data:        
        if censorship(data) is True:
            censored_user_list[data["company"]] = data["name"]
        else:
            pass
    return censored_user_list
        
def censorship(data):
    check = True
    if data['company'] in black_list:
        print(f'{data["company"]} 소속의 {data["name"]} 은 /는 등록할 수 없습니다.')
        check = False
    else:
        print('이상 없습니다.')
    return check

import requests 
# from pprint import pprint as print


dummy_data = []
for i in range(1, 11):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    response = requests.get(API_URL)
    parsed_data = response.json()
    if -80 < float(parsed_data['address']['geo']['lat']) < 80 and -80 < float(parsed_data['address']['geo']['lng']) < 80:
        temp_dummy_data = {
            'company': parsed_data['company']['name'],
            'lat': parsed_data['address']['geo']['lat'],
            'lng': parsed_data['address']['geo']['lng'],
            'name': parsed_data['name']
            }
        dummy_data.append(temp_dummy_data)            
       
print(create_user(dummy_data))


