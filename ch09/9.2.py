
def get_odds():
    for i in range(1, 10, 2):
        yield i

num = 0
for odd in get_odds():
    num += 1
    if num == 3:
        print(odd)