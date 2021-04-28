
secret, guess = map(int, input("1~10 사이의 숫자를 두 개 입력하세요\n").split())

if guess < secret:
    print("too low")
elif guess == secret:
    print("just right")
else:
    print("too high")