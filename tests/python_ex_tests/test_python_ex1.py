from exercises.python_exercises.python_ex1 import string_to_number


def test_string_to_number():
    assert string_to_number("1234") == 1234
    assert string_to_number("605") == 605
    assert string_to_number("14.05") == 14.05
    assert string_to_number("-7") == -7


def test_string_to_number2():
    assert string_to_number("1234") == 1234
    assert string_to_number("605") == 605
    assert string_to_number("14.05") == 14.05
    assert string_to_number("-7") == -7
