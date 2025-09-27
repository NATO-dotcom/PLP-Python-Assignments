# 1. Create and write into notes.txt
file = open("notes.txt", "w")
file.write("Line 1: Hello, World!\n")
file.write("Line 2: Python File Handling is fun!\n")
file.write("Line 3: Let's practice writing to files.\n")
file.close()

# 2. Read the entire content of the file
file = open("notes.txt", "r")
content = file.read()
print("📂 File Content After Writing:")
print(content)
file.close()

# 3. Append a new line to the file
file = open("notes.txt", "a")
file.write("Line 4: This line was appended.\n")
file.close()

# Reopen to confirm the appended line
file = open("notes.txt", "r")
updated_content = file.read()
print("📂 File Content After Appending:")
print(updated_content)
file.close()

# 4. Try to open a file entered by the user
filename = input("Enter the file name you want to read: ")
try:
    with open(filename, "r") as f:
        print("📂 Content of", filename)
        print(f.read())
except FileNotFoundError:
    print("❌ Error: The file you are trying to open does not exist.")


# 5. Division with error handling
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("✅ Result:", result)
except ZeroDivisionError:
    print("❌ Error: Division by zero is not allowed.")
except ValueError:
    print("❌ Error: Please enter valid numbers only.")
finally:
    print("Program finished!")
