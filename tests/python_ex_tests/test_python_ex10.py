from exercises.python_exercises.python_ex10 import century


def test_century():
    print('Testing for year 1705')
    assert century(1705) == 18
    print('Testing for year 1900')
    assert century(1900) == 19
    print('Testing for year 1601')
    assert century(1601) == 17
    print('Testing for year 2000')
    assert century(2000) == 20
    print('Testing for year 356')
    assert century(356) == 4
    print('Testing for year 89')
    assert century(89) == 1
