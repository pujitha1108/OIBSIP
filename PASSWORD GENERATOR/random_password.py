# random_password_generator.py

import string
import secrets  # safer random for passwords

def get_user_choices():
    print("Hello! Let's make a password.")
    # Ask for length
    while True:
        length_input = input("How many characters? (e.g., 12): ").strip()
        if length_input.isdigit() and int(length_input) > 0:
            length = int(length_input)
            break
        else:
            print("Please type a positive number, like 12.")

    # Ask for character types
    use_letters = input("Use letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Use numbers? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Use symbols? (y/n): ").strip().lower() == 'y'

    # Validate at least one type chosen
    if not (use_letters or use_numbers or use_symbols):
        print("We need at least one type! I'll add letters for you.")
        use_letters = True

    return length, use_letters, use_numbers, use_symbols

def build_character_pool(use_letters, use_numbers, use_symbols):
    pool = ""
    if use_letters:
        pool += string.ascii_letters
    if use_numbers:
        pool += string.digits
    if use_symbols:
        pool += string.punctuation

    return pool

def generate_password(length, pool):
    if not pool:
        raise ValueError("Character pool is empty.")
    # Use secrets.choice for strong randomness
    return ''.join(secrets.choice(pool) for _ in range(length))

def main():
    length, use_letters, use_numbers, use_symbols = get_user_choices()
    pool = build_character_pool(use_letters, use_numbers, use_symbols)

    # Optional: basic security rule—ensure at least one of each chosen type appears
    password_chars = []
    if use_letters:
        password_chars.append(secrets.choice(string.ascii_letters))
    if use_numbers:
        password_chars.append(secrets.choice(string.digits))
    if use_symbols:
        password_chars.append(secrets.choice(string.punctuation))

    # Fill the rest
    while len(password_chars) < length:
        password_chars.append(secrets.choice(pool))

    # Shuffle so first characters aren’t predictable
    # secrets doesn't have shuffle; use random.SystemRandom for secure shuffle
    sr = secrets.SystemRandom()
    sr.shuffle(password_chars)

    password = ''.join(password_chars[:length])
    print("\nYour password is:\n", password)

if __name__ == "__main__":
    main()
