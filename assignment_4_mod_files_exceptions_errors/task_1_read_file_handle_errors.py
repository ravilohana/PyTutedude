"""

Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.

Expected Output:

If the file exists:
Reading file content:
Line 1: This is a sample text file.
Line 2: It contains multiple lines.

If the file does not exist:
Error: The file 'sample.txt' was not found.
"""

# r_file variable is none because in finally block r_file throwing undefined for same, so defining it global level
# in finally block I am checking for None and then closing the file
# this can be avoided if I use keyword with, so in this case I do not need of finally block


"""
# without with keyword
r_file = None
try:
    r_file = open("data/sample1.txt", "r")
    file_contents = r_file.readlines()
    for i in range(0,len(file_contents)):
        print(f"Line {i+1}: {file_contents[i].strip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
finally:
    if r_file is not None:
        r_file.close()
        
        
"""
# used with keyword
try:
    with open("data/sample.txt", "r") as r_file:
        file_contents = r_file.readlines()
    for i in range(0,len(file_contents)):
        print(f"Line {i+1}: {file_contents[i].strip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
