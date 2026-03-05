"""

Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.
 Expected Output:
The output should include the result of each operation performed, for example:
Enter the first number: 5
Enter the second number: 10
Addition: 15
Subtraction: -5
Multiplication: 50
Division: 0.5


"""

user_input_a = int(input("Please enter the first number: "))
user_input_b = int(input("Please enter the second number: "))
addition = user_input_a + user_input_b
subtraction = user_input_a - user_input_b
multiplication = user_input_a * user_input_b
division = user_input_a / user_input_b
print("Addition: ", addition, "\n"
                              "Subtraction: ", subtraction, "\n"
                              "Multiplication: ", multiplication, "\n"
                               "Division: ", division,"\n"
    )
