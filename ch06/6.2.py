
guess_me = 7
number = 1

while True:
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
    elif number < guess_me:
        print("opps")
    number += 1