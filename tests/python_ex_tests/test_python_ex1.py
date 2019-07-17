def test_string_to_number():
	assert string_to_number("1234") == 1234
	assert string_to_number("605") == 605
	assert string_to_number("14.05") == 14.05
	assert string_to_number("-7") == -7