from exercises.python_exercises.python_ex2 import reverseWords


def test_reverseWords():
	assert reverseWords("hello world!") == "world! hello"