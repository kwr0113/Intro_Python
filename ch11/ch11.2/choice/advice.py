
from random import choice

answer = ['Yes!', 'No!', 'Reply hazy', 'what?']


def give():
    """임의의 대답을 반환"""
    return choice(answer)
