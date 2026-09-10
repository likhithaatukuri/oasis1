import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    character_pool = ""

    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        return "Error: No character types selected."

    return ''.join(random.choice(character_pool) for _ in range(length))

def main():
    try:
        length = int(input("Enter password length: "))
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        print("Generated password:", password)

    except ValueError:
        print("Invalid input. Please enter a number for the password length.")

main()
