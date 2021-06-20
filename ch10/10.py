# 10. 객체와 클래스


# 10.2.1 클래스 선언하기

class Cat:
    pass


a_cat = Cat()
another_cat = Cat()

# 10.2.2 속성

print(a_cat)
a_cat.age = 3
a_cat.name = 'Mr.fuzzybuttons'
a_cat.nemesis = another_cat

print(a_cat.name)
# print(a_cat.nemesis.name)     # Error

another_cat.name = 'Mr.Big'
print(another_cat.name)


class Cat:
    def __init__(self, name):
        self.name = name


furball = Cat('Grumpy')
print(furball.name)


# 10.3 상속
class Car:
    def exclaim(self):
        print("I'm a Car!")

    pass


class Yugo(Car):
    pass


print(issubclass(Car, Yugo), issubclass(Yugo, Car))

give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_car.exclaim()
give_me_a_yugo.exclaim()


# 10.3.2 메서드 오버라이드
class Car:
    def exclaim(self):
        print("I'm a Car!")


class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo!!!!!")


give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_car.exclaim()
give_me_a_yugo.exclaim()


class Person:
    def __init__(self, name):
        self.name = name


class MDPerson(Person):
    def __init__(self, name):
        self.name = 'Doctor ' + name


class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ', Esquire'


person = Person('Fudd')
doctor = MDPerson('Fudd')
laywer = JDPerson('Fudd')

print(person.name)
print(doctor.name)
print(laywer.name)


# 10.3.3 메서드 추가하기
class Car:
    def exclaim(self):
        print("I'm a Car!")


class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo!!!!!")

    def need_a_push(self):
        print("A little help here?")


give_me_a_car = Car()
give_me_a_yugo = Yugo()

# give_me_a_car.need_a_push()
give_me_a_yugo.need_a_push()


# 10.3.4 부모에게 도움받기 super()
class Person:
    def __init__(self, name):
        self.name = name


class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email


bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
print(bob.name)
print(bob.email)


# 10.3.5 다중 상속
class Animal:
    def says(self):
        return 'I speak!'


class Hores(Animal):
    def says(self):
        return 'Neigh!'


class Donkey(Animal):
    def says(self):
        return 'Hee-haw!'


class Mule(Donkey, Hores):
    pass


class Hinny(Hores, Donkey):
    pass


print(Mule.mro())
print(Hinny.mro())

mule = Mule()
hinny = Hinny()
print(mule.says(), hinny.says())


# 10.5.2 Getter/Setter 메서드
class Duck:
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print('inside the getter')
        return self.hidden_name

    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name


print('ee')
don = Duck('Donald')
print(don.get_name())
don.name = 'Donna'
print(don.get_name())
print('ee')


# 10.5.3 속성 접근을 위한 프로퍼티
class Duck:
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print('inside the getter')
        return self.hidden_name

    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

    name = property(get_name, set_name)  # 이거 추가해서 그냥 don.name으로도 접근 가능해짐


don = Duck('Donald')
print(don.get_name())
# don.set_name('Donna')
don.name = 'dondon'
print(don.get_name())


# 데코레이터
class Duck:
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name


don2 = Duck('Donald')
print(don2.name)
# don2.set_name('Donna')
don2.name = 'donon'
print(don2.name)


# 10.5.4 계산된 값의 프로퍼티
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius


c = Circle(5)
print(c.radius)
print(c.diameter)


# 10.5.5 네임 맹글링
class Duck:
    def __init__(self, input_name):
        self.__name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.__name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name


fowl = Duck('Howard')
print(fowl.name)
fowl.name = 'Donald'
print(fowl.name)


# 10.6 메서드 타입
# 인스터드 메서드          # 첫번째 인수 self
# 클래스 메서드           # 클래스 전체에 영향을 미치는 메서드
class A:
    count = 0

    def __init__(self):
        A.count += 1

    def exclaim(self):
        print("I'm an A!")

    @classmethod
    def kids(cls):
        print("A has", cls.count, 'little objects')


easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()
print(A.count)


# 정적 메서드                # 클래스나 객체에 영향을 미치지 않음. 편의를 위해 존재
class CoyoteWeapon:
    @staticmethod
    def commercial():
        print('this blahblah')


CoyoteWeapon.commercial()


# 10.7 덕 타이핑
class Quote:
    def __init__(self, person, words):
        self.person = person
        self.words = words

    def who(self):
        return self.person

    def says(self):
        return self.words + "."


class QuestionQuote(Quote):
    def says(self):
        return self.words + "?"


class ExclamationQuote(Quote):
    def says(self):
        return self.words + "!"


hunter = Quote('Elmer', "I'm hunting wabits")
print(hunter.who(), "says:", hunter.says())

hunter2 = QuestionQuote('Bugs', "What's up, doc")
print(hunter2.who(), "says:", hunter2.says())

hunter3 = ExclamationQuote('Daffy', "I's rabbit season")
print(hunter3.who(), "says:", hunter3.says())


class Babbling:
    def who(self):
        return 'Brook'

    def says(self):
        return 'Babble'


brook = Babbling()


def who_saying(obj):
    print(obj.who(), 'says', obj.says())


who_saying(hunter)
who_saying(hunter2)
who_saying(hunter3)
who_saying(brook)


# 10.8 매직 메서드
class Word:
    def __init__(self, text):
        self.text = text

    def equals(self, word2):
        return self.text.lower() == word2.text.lower()


first = Word('ha')
second = Word('HA')
third = Word('eh')

print(first.equals(second))
print(first.equals(third))


class Word:
    def __init__(self, text):
        self.text = text

    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()


first = Word('ha')
second = Word('HA')
third = Word('eh')

print(first == second)
print(first == third)


class Word:
    def __init__(self, text):
        self.text = text

    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

    def __str__(self):
        return self.text

    def __repr__(self):
        return 'word("' + self.text + '")'


first = Word('ha')
print(first)
print(first.__repr__())


# 애그리게이션과 콤퍼지션
class Bill:
    def __init__(self, description):
        self.description = description


class Tail:
    def __init__(self, length):
        self.length = length


class Duck:
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print("This duck has a", self.bill.description, "bill and a", self.tail.length, 'tail.')


a_tail = Tail('long')
a_bill = Bill('wide orange')
duck = Duck(a_bill, a_tail)
duck.about()


from collections import namedtuple

Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
print(duck)
print(duck.bill)
print(duck.tail)

