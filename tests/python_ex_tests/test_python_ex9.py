from IPython.core.tests.test_oinspect import Test

from exercises.python_exercises.python_ex9 import update_light


def test_update_light():
	assert (update_light('green'), 'yellow')
Test.assert_equals(update_light('yellow'), 'red')
Test.assert_equals(update_light('red'), 'green')