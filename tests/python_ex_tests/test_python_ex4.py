from ja_lp.exercises.python_exercises.python_ex4 import positive_sum


def test_positive_sum_examples():
    print("works for some examples")
    assert positive_sum([1, 2, 3, 4, 5]) == 15
    assert positive_sum([1, -2, 3, 4, 5]) == 13
    assert positive_sum([-1, 2, 3, 4, -5]) == 9


def test_positive_sum_empty_array():
    print("returns 0 when array is empty")
    assert positive_sum([]) == 0


def test_positive_sum_negative():
    print("returns 0 when all elements are negative")
    assert positive_sum([-1, -2, -3, -4, -5]) == 0
