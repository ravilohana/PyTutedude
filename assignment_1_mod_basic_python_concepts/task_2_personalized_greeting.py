"""
Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
Expected Output:
The program should output a greeting like:
Enter your first name: John
Enter your last name:
Hello, John Doe! Welcome to the Python program.

"""

user_first_name = input("Please enter your first name: ")
user_last_name = input("Please enter your last name: ")
full_name = user_first_name + " " + user_last_name
print(f"Hello, {full_name}! Welcome to the Python program.")
