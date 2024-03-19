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

def hw3_20(self):
	pass

if __name__ == '__main__':
	test_method = hw3_20
	args = [Student("Billy", "Johnson", 15),
			Student("Betty", "Bepot", 17),
			Student("Michael", "Jordan", 20),
			Student("Rose", "Gammine", 16),
			Student("Kevin", "Faire", 13)]

	expected = args[2]

	method_name = test_method.__name__

	result = test_method(args)
	print(f"Calling {method_name}({args})")

	print(f"Result: {result == expected} Returned: {result} Expected: {expected}")
	