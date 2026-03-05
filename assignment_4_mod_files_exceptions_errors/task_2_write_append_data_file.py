"""
Task 2: Write and Append Data to a File

Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.


Expected Output:
For example, if the user enters 25, the output should be:
Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.

Enter additional text to append: Learning file handling in Python.
Data successfully appended.

Final content of output.txt:
Hello, Python!
Learning file handling in Python.

"""

def write_data_file():
    try:
        user_data = input("Enter text to write to the file : ")
        with open("data/output.txt", "wt") as file:
            file.write(user_data+"\n")
        print("Data successfully written to 'output.txt'.")
    except FileNotFoundError:
        print("Error: The file 'output.txt' was not found.")

def append_data_file():
    try:
        user_data = input("Enter additional text to append : ")
        with open("data/output.txt", "a") as file:
            file.write(user_data + "\n")
        print("Data successfully appended to 'output.txt'.")
    except FileNotFoundError:
        print("Error: The file 'output.txt' was not found.")

def read_display_data_file():
    try:
        with open("data/output.txt", "r") as file:
            file_data = file.readlines()
            print("Final content of output.txt:")
            for data in file_data:
                print(data.strip())
    except FileNotFoundError:
        print("Error: The file 'output.txt' was not found.")




print(f"\n{'*'*25}")
print(f"{' '*5}File Operation")
print(f"{'*'*25}\n")
print(f"{'*'*5}\tNote: Writing to a file will overwrite existing data in the same file.\t{'*'*5}")
print("1. Write text to a file")
print("2. Enter additional text to append to the same file")
print("3. Read and display the contents of the file")
print("4. Exit")
while True:
    user_choice = input("Enter your choice: ")
    if user_choice == '1':
        write_data_file()
    elif user_choice == '2':
        append_data_file()
    elif user_choice == '3':
        read_display_data_file()
    elif user_choice == '4':
        print("4. Exit")
        break
    else:
        print("Please enter a valid choice!")

