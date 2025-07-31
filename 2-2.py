#문자열 인덱스 - 몇번째 글자야?
a = "Life is too short, You need Python"
print(a[3])

#문자열 슬라이싱 응용 - 문자 나누기
a = "20230331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)

#문자열 포매팅
#문자열 포맷코드 %d = 숫자, %s=문자
a="I eat %d apples." % 3
print(a)

#두 개 이상의 값 대입하기
number = 6
day = "three"
a="I ate %d apples. so I was sick for %s days." % (number, day)
print(a)