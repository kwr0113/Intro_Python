
def test_decorator(func):
    def dedeco(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return dedeco


@test_decorator
def test():
    print('this is func')

test()
