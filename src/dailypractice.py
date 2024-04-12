from typing import Any

def hw2_28(numbers: list):

	result = [num for num in numbers if num < 0]
	return result

def hw3_06(receivedDict: dict):
	# outcome = {key:val for (key, val) in receivedDict.items() if type(key) == int}
	# return list(outcome.values())

	outcome = [val for (key, val) in receivedDict.items() if type(key) == int]
	return outcome

class Student:
	"""docstring for Student"""
	def __init__(self, firstName: str, lastName: str, age: int):
		self.firstName = firstName
		self.lastName = lastName
		self.age = age

# Write a function that returns the age of a student
def returnAge(student: Student):
	return student.age

def hw3_13(listOfStudents: list[Student]) -> Student:

	outcome = max(listOfStudents, key=returnAge)
	return outcome

def hw3_20(listOfValues: list[Any]):
	counter = {}

	for value in listOfValues:
		if value in counter:
			counter[value] += 1
		elif value not in counter:
			counter[value] = 1

	outcome = max(counter, key=lambda k: counter[k])
	return outcome

def hw4_12(numbers: int):
	arr = []
	lengthNumbers = len(numbers)

	for index in range(lengthNumbers):
		if index == 0:
			result = numbers[index]
			arr.append(result)
		else:
			result = numbers[index] + numbers[index - 1] 
			arr.append(result)

	return arr

if __name__ == '__main__':
	test_method = hw4_12

	args = [3, 2, 4, 6]
	expected = [3, 5, 6, 10]

	method_name = test_method.__name__
	result = test_method(args)

	print(f"\nCalling {method_name}({args})")
	print(f"Result: {result == expected}, Returned: {result}, Expected: {expected}")