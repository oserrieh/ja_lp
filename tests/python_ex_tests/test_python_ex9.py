def test_update_light():
	assert update_light('green'), 'yellow')
Test.assert_equals(update_light('yellow'), 'red')
Test.assert_equals(update_light('red'), 'green')