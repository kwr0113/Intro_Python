
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
