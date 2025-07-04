import random
import string

def generate_password(length, use_upper, use_digits, use_symbols):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        return "Error: No character sets selected."

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# --- User Input ---
try:
    length = int(input("Enter password length: "))
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    result = generate_password(length, use_upper, use_digits, use_symbols)
    print(f"\nGenerated Password: {result}")

except ValueError:
    print("Invalid input. Please enter a valid number for length.")
