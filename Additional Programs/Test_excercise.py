import random
import pytest
from random import randint

def add_two_numbers(a, b):
    return a + b

def test_add_two_numbers():
    a = 5
    b = 5
    expected = 10

    actual = add_two_numbers(a, b)

    assert expected == actual

#test_add_two_numbers()


def get_random_number():
    return random.randint(1, 10)
#add getrenadom dependency
def add_number_with_random_number(a, get_random_number):
    return a + get_random_number()

def test_add_number_with_random_number():
    expected = 18
    a = 10


    def mock_get_random_number():
        return 8
                                        #uses mock get as pass in
    actual = add_number_with_random_number(a, mock_get_random_number)

    assert expected == actual

test_add_number_with_random_number()




def get_random_number():
    return randint(1, 10)

def add_two_random_numbers(get_random_number):
    return get_random_number() + get_random_number()


def test_add_two_random_numbers():
    expected = 16

    def mock_random_number():
        return 8

    actual = add_two_random_numbers(mock_random_number)

    assert expected == actual

test_add_two_random_numbers()


# def get_random_number():
#     return randint(1,10)

# def test_get_random_number():
#     expected = 7
#     def mock_rand():
#         return 6(1,10)




#mocking and stubbing
