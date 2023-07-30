import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/1'
# API 요청
response = requests.get(API_URL)
# JSON -> dict 데이터 변환
parsed_data = response.json()

# 응답 데이터 출력
print(response)

# 변환 데이터 출력
print(parsed_data)
# 변환 데이터의 타입
print(type(parsed_data))

# 특정 데이터 출력
print(parsed_data['name'])
print(parsed_data['username'])
print(parsed_data['company']['name'])

#리스트안에 리스트가 포함될수 있다
#딕셔너리또한 딕셔너리가 포함될수 있다
#딕서너리 속의 딕셔너리를 탐색하는것은, 리스트 속의 리스트를 탐색하는것과 방법이 같다