
def get_odds():
    for i in range(10):
        if i % 2 == 1:
            yield i

num = 0
for odd in get_odds():
    num += 1
    if num == 3:
        print(odd)