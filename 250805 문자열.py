#f 문자열 포매팅
name = '홍길동'
age = 30
a = f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
print(a)

#문자열 관련 함수들(매쏘드)
a = ", ".join('abcd')
print(a)

a=" to the ". join('jw')
print(a)

#문자열 바꾸기
a="life is too short"
print(a.replace("life", "Your leg"))

#문자열 나누기
a = "Life is too short"
print(a.split())

b = "a:b:c:d"
print(b.split(':'))
