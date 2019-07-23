from exercises.python_exercises.python_ex7 import reverse_list


def test_reverse_list():
    assert reverse_list([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert reverse_list([3, 1, 5, 4]) == [4, 5, 1, 3]
