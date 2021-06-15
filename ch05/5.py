
# \' \"를 이용하여 '와 "를 표현 가능

testimony = "\"I did nothing!\" he said."
print(testimony)


a = "hello"
b = "my name is"
c = "Python"

print(a + b + c)    # 연속 출력
print(a, b, c)      # 각 인수 사이에 공백을 붙임


start = "hi " * 2
middle = "hello" * 3 + "\n"
end = "Goodbye"

print(start + middle + end)


name = "Henny"
# name[0] = "P"
name = 'P' + name[1:]
name = name.replace("n", "t")
print(name)


eng = "abcdefghijklmnopqrstuvwxyz"
print(eng[:])
print(eng[13:])
print(eng[:13])
print(eng[10:20])
print(eng[::-1])

python = "Hello, my name is Python!!, Nice to meet you!"
print(python.split())
print(python.split(" ", 3))
print(python.split(","))
print(python.split("!"))

fruits = ["apple", "grape", "strawberry", "banana"]
print(", ".join(fruits))
print("//".join(fruits))

flower = "The flower is yellow, and that flower is red."

print(flower.replace("flower", "bird"))
# The bird is yellow, and that bird is red.
print(flower)
# The flower is yellow, and that flower is red.
flower = flower.replace("flower", "bird", 1)
print(flower)
# The bird is yellow, and that flower is red.


sample1 = "www.sample.com"
sample2 = " www.sample.com  "

print(sample1.strip("cwmo"))
print(sample2)
print(sample2.strip())


poem = '''All that doth flow me cannot liquid name
or else would fire and water be the same;
But that is liquid which is the moist and wet'''

print(poem[:13])
print(len(poem))
print(poem.startswith('All'))
print(poem.endswith("we"))

print(poem.find('the'))
print(poem.index("the"))
print(poem.rfind('the'))
print(poem.rindex("the"))

print(poem.find('duck'))
# print(poem.index("duck"))
print(poem.rfind('duck'))
# print(poem.rindex("duck"))

print(poem.count("the"))
print(poem.isalnum())

print("ab".isalnum())


setup = "a DUCK goes into a bar..."

print(setup.strip("."))
print(setup.capitalize())
print(setup.title())
print(setup.upper())
print(setup.lower())
print(setup.swapcase())

print(setup.center(30))
print(setup.ljust(30))
print(setup.rjust(30))


print("%s" % 42)
print("%d" % 42)
print("%x" % 42)
print("%o" % 42)

print("%s" % 7.03)
print("%f" % 7.03)
print("%e" % 7.03)
print("%g" % 7.03)


actor = "Richard Gere"
cat = "Chester"
weight = 28
print("My wife's favorite actor is %s" % actor)
print("Our cat %s weighs %s pounds" % (cat, weight))

thing = "woodchuck"
print('%s' % thing)
print('%12s' % thing)
print('%+12s' % thing)
print('%-12s' % thing)
print('%.3s' % thing)
print('%12.3s' % thing)
print('%-12.3s' % thing)

thing = 98.6
print('%f' % thing)
print('%12f' % thing)
print('%+12f' % thing)
print('%-12f' % thing)
print('%.3f' % thing)
print('%12.3f' % thing)
print('%-12.3f' % thing)

thing = 9876
print('%d' % thing)
print('%12d' % thing)
print('%+12d' % thing)
print('%-12d' % thing)
print('%.3d' % thing)
print('%12.3d' % thing)
print('%-12.3d' % thing)

thing = "woodchuck"
place = "lake"
print('{}'.format(thing))
print('The {} is in the {}'.format(thing, place))
print('The {1} is in the {0}'.format(place, thing))
print('The {thing} is in the {place}'.format(thing="duck", place="bathtub"))
d = {'thing': "duck", 'place': "bathtub"}
print('The {0[thing]} is in the {0[place]}'.format(d))

thing = 'wraith'
place = 'window'
print('The {} is at the {}'.format(thing, place))
print('The wraith is at the window')
print('The {:10s} is at the {:10s}'.format(thing, place))
print('The {:<10s} is at the {:<10s}'.format(thing, place))
print('The {:^10s} is at the {:^10s}'.format(thing, place))
print('The {:>10s} is at the {:>10s}'.format(thing, place))
print('The {:!^10s} is at the {:!^10s}'.format(thing, place))
print('The {:t^10s} is at the {:t^10s}'.format(thing, place))

thing = 'wereduck'
place = 'werepond'
print(f'the {thing} is in the {place}')
print(f'The {thing.capitalize()} is in the {place.rjust(20)}')
print(f'The {thing:>20} is in the {place:.^20}')
print(f'{thing =}, {place =}')
print(f'{thing[-4:] =}, {place.title() =}')
print(f'{thing = :>4.4}')


