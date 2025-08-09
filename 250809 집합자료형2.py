#합집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 | s2)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1.union(s2))

#차집합
print(s1-s2)
print(s1.difference(s2))

#추가하기
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

#값 여러개 추가하기(update)
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)

#값 없애기(remove)
s1 = set([1, 2, 3])
s1.remove(2)
print(s1)