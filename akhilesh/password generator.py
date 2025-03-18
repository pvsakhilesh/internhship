import random
import string
def generate_password(length, complexity):
    if complexity == 1:
        characters = string.ascii_lowercase
    elif complexity == 2:
        characters = string.ascii_letters
    elif complexity == 3:
        characters = string.ascii_letters + string.digits
    elif complexity == 4:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid complexity level."
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
print("Welcome to the Password Generator!")
try:
    length = int(input("Enter the desired password length: "))
    print("Select the password complexity:")
    print("1. Lowercase letters only")
    print("2. Lowercase and uppercase letters")
    print("3. Letters and digits")
    print("4. Letters, digits, and punctuation")
    complexity = int(input("Enter the complexity level (1-4): "))
    password = generate_password(length, complexity)
    print(f"Your generated password is: {password}")
except ValueError:
    print("Invalid input! Please enter numerical values.")