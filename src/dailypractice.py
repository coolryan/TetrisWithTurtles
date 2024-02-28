

def hw2_28(numbers: list):

	result = [num for num in numbers if num < 0]
	return result


if __name__ == '__main__':
	test_method = hw2_28
	args = [1,2,-3,-5,3,-10]
	expected = [-3,-5,-10]

	method_name = test_method.__name__

	result = test_method(args)
	print(f"Calling {method_name}({args})")


	print(f"Result: {result == expected} Returned: {result} Expected: {expected}")
	