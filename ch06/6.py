
# while
count = 1
while count <= 5:
    print(count)
    count += 1

print()


# break
while True:
    stuff = input("String to capitalize [type q to quit]: ")
    if stuff == "q":
        break
    print(stuff.capitalize())

print()


# continue
while True:
    value = input("Integer, please [q to quit]: ")
    if value == "q": #종료
        break
    number = int(value)
    if number % 2 == 0: #짝수
        continue
    print(number, "squared is", number*number)

print()


# else
numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number2 = numbers[position]
    if number2 % 2 == 0:
        print("Found even number", number2)
        break
    position += 1
else: # break 문이 호출되지 않은 경우
    print('No even number found')

print()


# for, in
word = 'thud'
offset = 0
while offset < len(word):
    print(word[offset])
    offset += 1

for letter in word:
    print(letter)

print()


# break
word = 'thud'
for letter in word:
    if letter == 'u':
        break
    print(letter)

print()


# else
word = 'thud'
for letter in word:
    if letter == 'x':
        print("Eek! An 'x'!")
        break
    print(letter)
else:
    print("No 'x' in there.")

print()


# range()
for x in range(0, 3):
    print(x)
print(list(range(0, 3)))

for x in range(2, -1, -1):
    print(x)
print(list(range(2, -1, -1)))

print(list(range(0, 11, 2)))