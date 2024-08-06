import re

def is_submarine_sound(s):
    pattern = r'^(100+1+|01)+$'
    # re.match() 함수는 문자열의 시작부터 패턴과 일치하는지 확인한다
    return re.match(pattern, s) is not None

s = input().strip()
print("SUBMARINE" if is_submarine_sound(s) else "NOISE")
