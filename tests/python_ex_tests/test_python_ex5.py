from exercises.python_exercises.python_ex5 import summation


def test_summation():
    print('Summation')
    print('Should return the correct total')
    assert summation(1) == 1
    assert summation(8) == 36


