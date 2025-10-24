import random
import string

def password_generator():
    """
    A simple password generator that allows users to specify:
    - Password length
    - Whether to include special characters
    """
    
    print("=" * 50)
    print("          PASSWORD GENERATOR")
    print("=" * 50)
    
    # Get password length from user
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 4): "))
            if length < 4:
                print("Password length should be at least 4 characters. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Ask if user wants special characters
    while True:
        include_special = input("Include special characters? (y/n): ").lower().strip()
        if include_special in ['y', 'yes', 'n', 'no']:
            include_special = include_special in ['y', 'yes']
            break
        else:
            print("Please enter 'y' for yes or 'n' for no.")
    
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Create the pool of characters based on user choice
    if include_special:
        char_pool = lowercase + uppercase + digits + special_chars
        print("Character pool includes: lowercase, uppercase, digits, and special characters")
    else:
        char_pool = lowercase + uppercase + digits
        print("Character pool includes: lowercase, uppercase, and digits")
    
    # Generate password ensuring at least one character from each required category
    password = []
    
    # Ensure at least one lowercase
    password.append(random.choice(lowercase))
    
    # Ensure at least one uppercase
    password.append(random.choice(uppercase))
    
    # Ensure at least one digit
    password.append(random.choice(digits))
    
    # If special characters are included, ensure at least one
    if include_special:
        password.append(random.choice(special_chars))
    
    # Fill the rest of the password length with random characters from the pool
    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(random.choice(char_pool))
    
    # Shuffle the password to randomize the positions of required characters
    random.shuffle(password)
    
    # Convert list to string
    final_password = ''.join(password)
    
    # Display the generated password
    print("\n" + "=" * 50)
    print("GENERATED PASSWORD:")
    print(f"Length: {len(final_password)} characters")
    print(f"Password: {final_password}")
    print("=" * 50)
    
    return final_password

def main():
    """
    Main function to run the password generator
    """
    while True:
        password = password_generator()
        
        # Ask if user wants to generate another password
        while True:
            again = input("\nGenerate another password? (y/n): ").lower().strip()
            if again in ['y', 'yes', 'n', 'no']:
                break
            else:
                print("Please enter 'y' for yes or 'n' for no.")
        
        if again in ['n', 'no']:
            print("\nThank you for using the Password Generator!")
            break

if __name__ == "__main__":
    main()