import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_numbers=True, use_special=True):
    if length < 4:
        print("Password length should be at least 4 characters for better security.")
        return None

    char_pool = ""
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_lowercase:
        char_pool += string.ascii_lowercase
    if use_numbers:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation

    if not char_pool:
        print("You must select at least one character type!")
        return None

    # Generate a secure random password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    print("Welcome to PassForge: Secure Password Generator")
    while True:
        try:
            length = int(input("Enter password length (minimum 4): "))
            use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == "y"
            use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == "y"
            use_numbers = input("Include numbers? (y/n): ").strip().lower() == "y"
            use_special = input("Include special characters? (y/n): ").strip().lower() == "y"
            
            password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special)
            if password:
                print(f"Generated Password: {password}")
            
            another = input("Generate another password? (y/n): ").strip().lower()
            if another != "y":
                print("Goodbye!")
                break
        except ValueError:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
