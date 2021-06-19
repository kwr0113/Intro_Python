
def test_decorator(func):
    print('start')
    func()
    print('end')


@test_decorator
def test():
    print('this is func')

test()
