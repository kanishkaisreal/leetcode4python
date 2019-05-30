# Python program to reverse a
# string with special characters

# Returns true if x is an aplhabatic
# character, false otherwise

# This problem was asked by Facebook.

# Given a string and a set of delimiters, reverse the words in the string while maintaining the relative order of the delimiters. For example, given "hello/world:here", return "here/world:hello"

# Follow-up: Does your solution work for the following cases: "hello/world:here/", "hello//world:here"


# https://www.geeksforgeeks.org/reverse-an-array-without-affecting-special-characters/

def isAlphabet(x):
	return x.isalpha()


def reverse(string):
	LIST = toList(string)

	# Initialize left and right pointers
	r = len(LIST) - 1
	l = 0

	# Traverse LIST from both ends until
	# 'l' < 'r'
	while l < r:

		# Ignore special characters
		if not isAlphabet(LIST[l]):
			l += 1
		elif not isAlphabet(LIST[r]):
			r -= 1

		# Both LIST[l] and LIST[r] are not special
		else:
			LIST[l], LIST[r] = swap(LIST[l],LIST[r])
			l += 1
			r -= 1

	return toString(LIST)

# Utility functions


def toList(string):
	List = []
	for i in string:
		List.append(i)
	return List


def toString(List):
	return ''.join(List)


def swap(a, b):
	return b, a

if __name__ == '__main__':

	# Driver code
	# string = "a!!!b.c.d,e'f,ghi"
	# string = "a,b$c"
	string = 'hello/world:here/'  # it won't work for this string. 
	print("Input string: " + string)
	string = reverse(string)
	print("Output string: " + string)
