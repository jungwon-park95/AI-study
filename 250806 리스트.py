#리스트 슬라이싱
a=[1,2,3,4,5]
print(a[0::2])

#중첩된 리스트에서 슬라이싱
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])
print(a[3][:2])

#리스트 더하기
a=[1,2,3]
b=[4,5,6]
print(a+b)

#리스트의 삭제
a=[1,2,3]
del a[1]
print(a)

#삭제 + 슬라이싱
a=[1,2,3,4,5]
del a[2:4]
print(a)

#정렬
a = [1, 4, 3, 2]
a.sort()
print(a)

#역정렬
a = [1, 4, 3, 2]
a.reverse()
print(a)

#그럼 내림차순은?
a = [1, 4, 3, 2]
a.sort()
a.reverse()
print(a)

#원하는 자리에 삽입
a=[1,2,3]
a.insert(0,4)
print(a)

#pop 맨 마지막 자가 튀어나오는 것
a=[1,2,3]
a.pop()
print(a)
