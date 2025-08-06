dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(type(dic))

#딕셔너리에 키 추가하기
a={1:'a'}
a[2]='b'
print(a)

#딕셔너리에서 삭제하기, 키를 삭제해주면 됨
a={1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}
del a[1]
print(a)

#딕셔너리는 value를 얻기위해 Key를 입력한다
dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(dic['name'])

#Key 리스트 만들기 - keys
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.keys())

#해당 Key가 딕셔너리 안에 있는지 조사하기 - in
a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
print('name' in a)