
# 딕셔너리

# 생성하기 dict{}
empty_dict = {}
bierce = {
    "day": "A period of twenty_four hours, mostly misspent",
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The kind of fortune that never misses"
}
print(bierce)

acme_customer = {'first': 'wile', 'middle': 'E', 'last': 'Coyote'}
print(acme_customer)

acme_customer = dict(first='wile', middle='E', last='Coyote')
print(acme_customer)

# 변환하기 dict()       # 두 값으로 이루어진 시퀀스를 딕셔너리로 변환할 수 있다
lol = [['a', 'b'], ('c', 'd'), ['e', 'f']]
print(lol)
lol = dict(lol)
print(lol)

# 항목 추가/변경 [key]        # 딕셔너리의 키들은 반드시 고유해야 한다
pythons = {
    'Champman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric'
}
print(pythons)
pythons['Gilliam'] = 'Gerry'
print(pythons)
pythons['Gilliam'] = 'Terry'
print(pythons)

# 항목 얻기 [key]와 get()
print(pythons['Idle'])      # 딕셔너리에 키가 존재하지 않으면 예외가 발생
print('Teen' in pythons)
print(pythons.get("Teen"))  # 옵션이 없으면 None
print(pythons.get("Teen", 'Not a Python'))  # 지정한 옵션이 대신 출력
print('Idle' in pythons)
print(pythons.get("Idle"))

# 모든 키 얻기 keys() / 모든 값 얻기 values()
print(list(pythons.keys()))
print(list(pythons.values()))

# 모든 키-값 얻기 items()
print(list(pythons.items()))    # 각 키와 값은 튜플로 묶여서 반환

# 결합하기 {**a, **b}
first = {'a': 'agony', 'b': 'bliss'}
second = {'b': 'bagles', 'c': 'candy'}
third = {'d': 'donut'}

firsec = {**first, **second}
firsecthi = {**first, **second, **third}

print(firsec)
print(firsecthi)
firsec['b'] = 'bless'

print(first)
print(second)
print(firsec)
print(firsecthi)

# 결합하기 update()
print(pythons)
others = {'Mark': 'Groucho', 'Howard': 'Moe'}
pythons.update(others)
print(pythons)

# 딕셔너리 컴프리헨션
# {키_표현식 : 값_표현식 for 표현식 in 순회 가능한 객체}
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)
letter_counts2 = {letter: word.count(letter) for letter in set(word)}
print(letter_counts2)

vowels = 'aeiou'
word = 'onomatopoeia'
vowels_counts = {letter: word.count(letter) for letter in set(word) if letter in vowels}
print(vowels_counts)


# 셋

# 생성하기 set()
empty_set = set()
even_numbers = {0, 2, 4, 6, 8}
odd_numers = {1, 3, 5, 7, 9}

# 변환하기 set()
letters = set('letters')
print(letters)

# 항목 추가하기 add()
letters.add('k')
print(letters)

# 항목 삭제하기 remove()
letters.remove('k')
print(letters)

# 멤버십 테스트 in
drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahula'},
    'white russian': {'vodka', 'kahula', 'cream'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

print('//')

for name, contents in drinks.items():
    if 'vodka' in contents and 'vermouth' not in contents and 'cream' not in contents:
        print(name)

print('//')

for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)

# 불변 셋 frozenset()
fs = frozenset([1, 2, 3])
print(fs)
