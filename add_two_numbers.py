'''Addition: One common problem when prompting for numerical input occurs when people provide text instead of numbers. 
When you try to convert the input to an int, you’ll get a ValueError. Write a program that prompts for two numbers. 
Add them together and print the result. Catch the ValueError if either input value is not a number, and print a friendly error message. 
Test your program by entering two numbers and then by entering some text instead of a number.'''

def addition_of_two_nums():
	try:
		num1 = int(input("Enter first number : "))
		num2 = int(input("Enter second number : "))
	except ValueError:
		print("Sorry, please enter number instead of text.")
	else:
		result = num1 + num2
		print(result)
		
addition_of_two_nums()
