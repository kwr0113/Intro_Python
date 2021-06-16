import copy


# 튜플은 불변 immutable / 리스트는 가변 mutable

# 튜플 tuple

# 생성하기 ()
empty_tuple = ()            # 빈 튜플

# 단일 요소를 가진 튜플
one_marx = 'Groucho',       # tuple
one_marx = 'Groucho'        # str
one_marx = ('Groucho',)     # tuple
one_marx = ('Groucho')      # str

# 요소가 두 개 이상인 튜플. 마지막에 콤마를 붙이지 않는다
marx_tuple = 'Groucho', 'Chico', 'Harpo'
marx_tuple = ('Groucho', 'Chico', 'Harpo')

# 쉼표만 사용하여 단일 요소를 가진 튜플을 만들 수 있지만, 함수에 인수로 전달할 수 없다

# 튜플로 한번에 여러 변수 할당하기    # 튜플 언패킹
a, b, c = marx_tuple
print(a)
print(b)
print(c)

# 생성하기 tuple()
marx_list = ['Groucho', 'Chico', 'Harpo']
print(type(marx_list), marx_list)
marx_list = tuple(marx_list)
print(type(marx_list), marx_list)
another_empty_tuple = tuple()

# 결합하기 +
one = 'Groucho',
two = 'Chico', 'Harpo'
print(type(one), type(two))
three = one + two
print(type(three), three)

# 튜플의 오프셋 / 슬라이스
print(three[2])
# print(three[5])       # 오류 발생
print(three[:2])
print(three[5:7])       # 오류 발생하지 않고 빈 튜플을 반환

# 항목 복제하기 *
four = one * 3
print(type(four), four)


# 리스트 list

# 생성하기 []
empty_list = []
weekdays = ['monday', 'tuesday', 'wednsday', 'thursday', 'friday']
leep_years = [2000, 2000, 2004]

# 생성 및 변환하기 list()
another_empty_list = list()
cat = list('cat')       # 문자열str -> 리스트list
print(type(cat), cat)
weekdays = list(weekdays)
print(type(weekdays), weekdays)

# 문자열 분할로 생성하기 split()

# [offset]으로 항목 얻기
print(weekdays[0])
print(weekdays[3])
print(weekdays[-3])

# 슬라이스로 항목 얻기
print(weekdays[:2])
print(weekdays[1:3])
print(weekdays[::2])

# 리스트 뒤집기
reverse_weekdays_slice = weekdays[::-1]     # 원본 리스트를 뒤집어 복사본을 반환, 원본 리스트는 변경되지 않는다
print(weekdays)
print(reverse_weekdays_slice)
weekdays.reverse()                          # 원본 리스트를 뒤집어 저장, 원본 리스트가 변경되며 값을 반환하지 않는다
print(weekdays)

# 리스트의 오프셋 / 슬라이스
print(weekdays[2])
# print(weekdays[5])       # 오류 발생
print(weekdays[:2])
print(weekdays[5:7])       # 오류 발생하지 않고 빈 리스트를 반환

# 리스트 끝에 항목 추가하기 append()
marxs = ['Groucho', 'Chico', 'Harpo']
print(marxs)
marxs.append('Zeppo')
print(marxs)

# 리스트의 원하는 위치에 항목 추가하기 insert()
marxs.insert(2, 'Gummo')
print(marxs)
marxs.insert(10, 'Ropin')       # 리스트의 끝을 넘는 오프셋은 append() 처럼 끝에 항목을 추가
print(marxs)
marxs2 = marxs[:]

# 오프셋 / 슬라이스로 항목 바꾸기    # 튜플과 달리 가변적이라 항목을 바꿀 수 있음
marxs[3] = 'Wanda'
print(marxs)
marxs[2:5] = ['Groucho', 'Chico', 'Harpo']
print(marxs)
marxs[2:5] = "str"              # 리스트 외 순회 가능한 타입은 모두 가능
print(marxs)
marxs[2:5] = ('Groucho', 'Chico', 'Harpo')
print(marxs)

# 오프셋으로 항목 삭제하기 del
del marxs[-1]
print(marxs)
del marxs[2]
print(marxs)        # 중간의 특정 항목을 삭제하면 제거된 항목 이후의 항목들이 앞으로 한칸씩 당겨진다

# 값으로 항목 삭제하기 remove()
marxs.remove("Chico")
print(marxs)        # 리스트의 항목이 중복되면 첫번째 항목만 삭제

# 오프셋으로 항목을 얻은 후 삭제하기 pop()
print(marxs.pop())      # 인수가 없으면 default -1        # pop(0)은 리스트의 머리(시작)을, pop()/pop(-1)은 리스트의 꼬리(끝)을 반환/삭제
print(marxs)
print(marxs.pop(0))
print(marxs)

# 모든 항목 삭제하기 clear()
marxs.clear()
print(marxs)

# 값으로 오프셋 찾기 index()
print(marxs2.index('Chico'))            # 중복된 값이 있으면 첫번째 오프셋만 반환

# 존재여부 확인하기 in
print('Chico' in marxs2)
print('Chico' in marxs)

# 값 세기 count()
print(marxs2.count('Chico'))
print((marxs2 * 3).count('Chico'))

# 문자열로 변환하기 join()
print('*'.join(marxs2))

# 정렬하기 sort() / sorted()
print(marxs2)
print(sorted(marxs2))       # 원본 리스트를 정렬한 복사본을 반환, 원본 리스트는 변경되지 않는다
print(marxs2)
marxs2.sort()
print(marxs2)               # 원본 리스트를 오름차순으로 정렬
marxs2.sort(reverse=True)   # 내림차순으로 정렬 시 인수에 reverse=True 를 추가
print(marxs2)

# 항목 개수 얻기 len()
print(len(marxs2))

# 복사하기 copy(), list(), 슬라이스
a = marxs2.copy()
b = list(marxs2)
c = marxs2[:]
print(a)
print(b)
print(c)
marxs2.clear()
print(marxs2)
print(a)
print(b)
print(c)

# 깊은 복사하기 deepcopy()
marxs2 = [1, 2, [3, 4]]
a = marxs2.copy()
b = list(marxs2)
c = marxs2[:]
print(a, b, c)
marxs2[1] = 5
marxs2[2][1] = 10
print(marxs2)
print(a, b, c)

d = copy.deepcopy(marxs2)
marxs2[1] = 8
marxs2[2][1] = 9
print(marxs2)
print(d)

for k in marxs2:
    print(k)

# 여러 시퀀스 순회하기 zip()
days = ['Monday', 'Tuesday', 'Wednsday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
zz = zip(days, fruits, drinks, desserts)
for day, fruit, drink, dessert in zz:
    print(day, ": drink", drink, '- eat', fruit, '- enjoy', dessert)

print(type(zz))
print(zz)

for i in zz:
    print(i)

print(dict(zip(days, fruits)))

# 리스트 컴프리헨션
# [표현식 for 항목 in 순회 가능한 객체]
number_list = [number for number in range(10)]
print(number_list)
# [표현식 for 항목 in 순회 가능한 객체 if 조건]
a_list = [number for number in range(20) if number % 2 == 0]
print(a_list)
