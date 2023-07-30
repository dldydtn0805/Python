# ws_4_2.py

import requests
from pprint import pprint as print

dummy_data = []

for i in range(1, 11):
# 무작위 유저 정보 요청 경로
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
# API 요청
    response = requests.get(API_URL)
# JSON -> dict 데이터 변환
    parsed_data = response.json()

    dummy_data.append(parsed_data['name'])

print(dummy_data)

#fstring은 문자열이면 모두 사용 가능하다, 주소값에서도 가능하다
#append를 사용한다
