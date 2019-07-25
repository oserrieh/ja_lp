from exercises.python_exercises.python_ex3 import monkey_count


def test_monkey_count():
    assert monkey_count(5) == [1, 2, 3, 4, 5]
    assert monkey_count(3) == [1, 2, 3]
    assert monkey_count(9) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert monkey_count(10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert monkey_count(20) == [1, 2, 3, 4, 5, 6, 7, 8,
                                9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def test_monkey_count2():
    assert monkey_count(5) == [1, 2, 3, 4, 5]
    assert monkey_count(3) == [1, 2, 3]
    assert monkey_count(9) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert monkey_count(10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert monkey_count(20) == [1, 2, 3, 4, 5, 6, 7, 8,
                                9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
