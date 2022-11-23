import unittest

def add_two_numbers(a, b):
    return a + b

def test_add_two_numbers():
    a = 5
    b = 5
    expected = 10

    actual = add_two_numbers(a, b)

    assert expected == actual

def test_add_a_negative_numbers():
    a = 5
    b = -5
    expected = 0

    actual = add_two_numbers(a, b)

    assert expected == actual

def test_add_two_floating():
    a = 5.0
    b = 5.1
    expected = 10.1

    actual = add_two_numbers(a, b)

    assert expected == actual

#class MyTestCase(unittest.TestCase):
def test_add_num_and_string():
    a = "hi"
    b = 5
    expected = ValueError

    actual = add_two_numbers(a, b)

    assert expected == actual

test_add_two_numbers()
test_add_a_negative_numbers()
test_add_two_floating()
test_add_num_and_string()
# print (a)
# print (b)
# print (expected)