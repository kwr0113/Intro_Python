# 9.1 함수 정의하기 def

def do_nothing():
    pass


# 9.2 함수 호출하기 ()

do_nothing()


# 아무일도 일어나지 않음

def make_a_sound():
    print('quack')


make_a_sound()


# quack 이 출력됨

def agree():
    return True


if agree():
    print('Splendid!')
else:
    print('That was unexpected')


# True를 반환하는 함수기 때문에 Splendid가 출력


# 9.3 인수와 매개변수

def echo(anything):
    return anything + ' ' + anything


print(echo('Rumplestiltskin'))


# 함수로 전달한 값은 인수, 인수와 함수를 호출하면 인수의 값은 함수 내에서 해당하는 매개변수에 복사됨
# 함수 외부에서는 인수, 내부에서는 매개변수


def commentary(color):
    if color == 'red':
        return "It's a Tomato"
    elif color == "green":
        return "It's a green pepper"
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it"
    else:
        return "I've never heard of the color " + color + "."


comment = commentary("blue")
print(comment)

# 함수가 명시적으로 return을 호출하지 않으면, 호출자는 반환값으로 None을 얻음
print(do_nothing())

# 9.3.1 유용한 None

# 아무것도 없다는 것을 뜻하는 파이썬의 특별한 값
# False처럼 보이지만 다른 값

thing = None
if thing:
    print("It's some thing")
else:
    print("It's no thing")

if thing is None:
    print("It's nothing")
else:
    print("It's something")


# 빠뜨린 빈 값을 구분하기 위해 None을 사용
# 정수 0, 부동소수점 0.0, 빈 문자열 '', 빈 리스트[], 빈 튜플(), 빈 딕셔너리 {}, 빈 셋 set() 모두 False지만 None과 같지 않다


def whatis(things):
    if things is None:
        print(things, 'is None')
    elif things:
        print(things, 'is True')
    else:
        print(things, 'is False')


whatis(None)
whatis(True)
whatis(False)
whatis(0)
whatis(0.0)
whatis(' ')
whatis(())
whatis([])
whatis([0])


# 9.3.2 위치 인수

def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


print(menu('beef', 'bagle', 'bordeaux'))

# 9.3.3 키워드 인수
print(menu(entree='beef', dessert='bagle', wine='bordeaux'))
print(menu('frontenac', dessert='flan', entree='fish'))


# 위치 인수와 키워드 인수를 함께 사용하여 함수를 호출할 때는 위치 인수가 먼저 와야 한다


# 9.3.4 기본 매개변수 값 저장하기
def menu(wine, entree, dessert="pudding"):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


print(menu('chardonnay', 'chicken'))
print(menu('dunkelfelder', 'duck', 'doughnut'))


# 기본 인수는 함수가 정의될 때 계산된다
def buggy(arg, result=[]):
    result.append(arg)
    print(result)


buggy('a')
buggy('b')  # ['b']가 출력되지 않고 ['a']가 출력된다


def works(arg):
    result = []
    result.append(arg)
    print(result)


works('a')
works('b')


def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)
    return result


nonbuggy('a', nonbuggy('b'))


# 9.3.5 위치 인수 분해하기/모으기
# 애스터리스크 * : 함수의 매개변수에 사용하면 매개변수에서 위치 인수 변수를 튜플로 묶는다

def print_args(*args):
    print('Positional tuple:', args)


print_args()
print_args(3, 2, 1, 'Wait!', 'Uh.....')


def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one:', required2)
    print('All the rest:', args)


print_more('cap', 'glasses', 'scarf', 'monocle', 'mustache wax')


# 9.3.6 키워드 인수 분해하기/모으기
def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)


print_kwargs()
print_kwargs(wine='merlot', entree='mutton')


# 9.3.7 키워드 전용 인수
# * 이후의 인수들은 키워드를 입력하지 않고 위치 인수로 전달할 수 없다
def print_data(data, *, start=0, end=100):
    for value in (data[start:end]):
        print(value)


data = ['a', 'b', 'c', 'd', 'e', 'f']
# print_data(data, 4)   # 오류 발생
print_data(data, start=4)
print()

# 9.3.8 가변/불변 인수
outside = ['one', 'fine', 'day']


def mangle(arg):
    arg[1] = 'terrible'

print(outside)
mangle(outside)
print(outside)
# 안 좋은 예시


# 9.4 독스트링
def echo(anything):
    """echo returns its input argument"""
    return anything


def print_if_true(thing, check):
    """
    Prints the first argument if a second argument is true
    The operation is:
    """
    if check:
        print(thing)

help(echo)
print(echo.__doc__)


# 9.5 일등 시민

def answer():
    print(42)

answer()


def run_something(func):
    func()

run_something(answer)
# 42가 출력된다


def add_args(arg1, arg2):
    print(arg1+arg2)


def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)

run_something_with_args(add_args, 5, 9)


def sum_args(*args):
    return sum(args)


def run_with_positional_args(func, *args):
    return func(*args)

print(run_with_positional_args(sum_args, 1, 2, 3, 4))


# 9.6 내부 함수
def outer(a, b):
    def inner(c, d):
        return c+d
    return inner(a, b)

print(outer(4, 7))


# 9.6.1 클로저
# 외부 함수로부터 생성된 변수값을 변경하고, 저장할 수 있는 함수. 다른 함수에 의해 동적으로 생성됨
def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2

a = knights2('Duck')
b = knights2('Hasenpfeffer')

print(a, b)
print(type(a), type(b))


# 9.7 익명 함수 lambda
def edit_story(words, func):
    for word in words:
        print(func(word))

stairs = ['thud', 'meow', 'thud', 'hiss']


def enliven(word):
    return word.capitalize() + '!'

edit_story(stairs, enliven)
edit_story(stairs, lambda word: word.capitalize() + '!')


# 9.8.1 제너레이터
# 시퀀스를 생성하는 객체

def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

ranger = my_range(1, 5)
for x in ranger:
    print(x)
for x2 in ranger:
    print(x2)
# 제너레이터는 한 번 순회를 마치면 아무것도 반환하지 않는다

# 9.8.2 제너레이터 컴프리헨션
genobj = (pair for pair in zip(['a', 'b'], ['c', 'd']))
for thing in genobj:
    print(thing)


# 9.9 데커레이터
# 하나의 함수를 취해서 또 다른 함수를 반환하는 함수

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function: ', func.__name__)
        print('Positional arguments: ', args)
        print('Keyword arguments: ', kwargs)
        result = func(*args, **kwargs)
        print('Result: ', result)
        return result
    return new_function

a = document_it(print_data)
a('hello')


@document_it
def edit_story(words, func):
    for word in words:
        print(func(word))


# 9.10 네임스페이스와 스코프
def change_local():
    animal = 'wombat'
    print('inside change_local:', animal, id(animal))

change_local()
# print(animal)     # NameError

animal = 'fruitbat'


def change_and_print_global():
    global animal
    animal = 'wombat'
    print('after the change:', animal)

print(animal)
change_and_print_global()
print(animal)

animal = 'fruitbat'


def change_local():
    animal = 'wombat'
    print('locals:', locals())

print(animal)
change_local()
print('globals:', globals())


# 9.12 재귀함수
def dive():
    return dive()


def flatten(lol):
    for item in lol:
        if isinstance(item, list):
            for subitem in flatten(item):
                yield subitem
    else:
        yield item

loll = [1, 2, [3, 4, 5], [6, [7, 8, 9], []]]

# for i in flatten(loll):
#     print(i)
# print(list(flatten(loll)))
# 오류남 재귀함수 너무 많이 일어난다고.......

# 9.14.1 에러 처리하기

short_list = [1, 2, 3]
position = 5
try:
    short_list[position]
except:
    print('Need a position between 0 and', len(short_list)-1, 'but got', position)

while True:
    value = input('position [q to quit]? ')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad index: ', position)
    except Exception as other:
        print('Something else broke:', other)


# 9.14.2 예외 만들기
