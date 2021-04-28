
# \ 백슬래시 문자로 다음 줄로 이어서 입력 가능

sum = 1 + \
    2 + \
    3 + \
    4

print(sum)



# if, elif, else

disaster = True
if disaster:
    print('Woe!')
else:
    print('Whee!')


furry = True
large = True
if furry:
    if large:
        print("It's a yeti.")
    else:
        print("It's a cat!")
else:
    if large:
        print("It's a whale.")
    else:
        print("It's a human. Or a hairless cat.")


color = "mauve"
if color == "red":
    print("It's a tomato.")
elif color == "green":
    print("It's a green pepper.")
elif color == "bee purple":
    print("I don't know what it is, but only bees can see it")
else:
    print("I've never heard of the color", color)



# in 연산자

vowel_string = 'aeiou'
vowel_set = {'a', 'e', 'i', 'o', 'u'}
vowel_list = ['a', 'e', 'i', 'o', 'u']
vowel_tuple = ('a', 'e', 'i', 'o', 'u')
vowel_dict = {'a': 'apple', 'e': 'elephant', 'i': 'impala', 'o': 'ocelot', 'u': 'unicorn'}
letter = 'o'

print(letter in vowel_string)
print(letter in vowel_set)
print(letter in vowel_list)
print(letter in vowel_tuple)
print(letter in vowel_dict)



# := 바다코끼리 연산자

walrus = "walrus operator"
n1 = len(walrus)
if n1 > 5:
    print("kkk")

if n2 := len(walrus) > 5:
    print("kkk")