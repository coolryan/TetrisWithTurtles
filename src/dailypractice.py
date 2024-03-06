

def hw2_28(numbers: list):

	result = [num for num in numbers if num < 0]
	return result

def hw3_06(receivedDict: dict):
	# outcome = {key:val for (key, val) in receivedDict.items() if type(key) == int}
	# return list(outcome.values())

	outcome = [val for (key, val) in receivedDict.items() if type(key) == int]
	return outcome

if __name__ == '__main__':
	test_method = hw3_06
	args = {1:2,-3:-5,3:-10}
	expected = [2,-5,-10]

	method_name = test_method.__name__

	result = test_method(args)
	print(f"Calling {method_name}({args})")

	print(f"Result: {result == expected} Returned: {result} Expected: {expected}")
	