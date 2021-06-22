
# 누락된 키 처리하기 setdefalt() defaultdict()

periodic_table = {'Hydrogen': 1, 'Helium': 2}
carbon = periodic_table.setdefault('Carbon', 12)
print(carbon)
print(periodic_table)

helium = periodic_table.setdefault('Helium', 947)
print(helium)
print(periodic_table)


from collections import defaultdict, OrderedDict

periodic_table = defaultdict(int)
periodic_table['Hydrogen'] = 1
print(periodic_table['Lead'])
print(periodic_table)


def no_idea():
    return 'Huh?'

bestiary = defaultdict(no_idea)
bestiary = defaultdict(lambda: 'Huh?')

bestiary['A'] = 'Abominable snowman'
bestiary['B'] = "Basilisk"
print(bestiary['A'])
print(bestiary['B'])
print(bestiary['C'])


food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1

for food, count in food_counter.items():
    print(food, count)


from collections import Counter

breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
# 항목 개수 출력
print(breakfast_counter)
# 항목 개수 내림차순 출력, 인수로 숫자를 전달하면 그 숫자만큼 상위 요소를 반환
print(breakfast_counter.most_common())
print(breakfast_counter.most_common(1))
# 카운터는 결합이 가능
lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
print(lunch_counter)

plus = lunch_counter + breakfast_counter
print(plus)
print(plus.most_common(1))
minus = lunch_counter - breakfast_counter
print(minus)

print(breakfast_counter & lunch_counter)
print(breakfast_counter | lunch_counter)


def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

print(palindrome('a'))
print(palindrome('racecar'))
print(palindrome(''))
print(palindrome('radar'))
print(palindrome('hailbut'))


def another_palindrome(word):
    return word == word[::-1]

print(another_palindrome('radar'))
print(another_palindrome('hailbut'))


import itertools
for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)

# for item in itertools.cycle([1, 2]):
#    print(item)

for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)


def multiply(a, b):
    return a * b

for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)


from  pprint import pprint
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!')
])

print(quotes)
pprint(quotes)

from random import choice
print(choice(range(100)))

from random import sample
print(sample(range(100), 4))

from random import randint
print(randint(10, 20))

from random import randrange
print(randrange(10, 20, 2))

from random import random
print(random())