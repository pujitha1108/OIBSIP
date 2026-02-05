# gui_password_generator.py

import tkinter as tk
from tkinter import messagebox
import string
import secrets

def build_pool(use_letters, use_numbers, use_symbols, exclude_chars):
    pool = ""
    if use_letters:
        pool += string.ascii_letters
    if use_numbers:
        pool += string.digits
    if use_symbols:
        pool += string.punctuation

    # Remove excluded characters
    if exclude_chars:
        pool = ''.join(ch for ch in pool if ch not in exclude_chars)

    return pool

def generate_secure_password(length, use_letters, use_numbers, use_symbols, exclude_chars):
    # Validate length
    if length <= 0:
        raise ValueError("Length must be positive.")

    pool = build_pool(use_letters, use_numbers, use_symbols, exclude_chars)

    if not pool:
        raise ValueError("No characters available. Adjust your options.")

    # Security rule: if a type is selected, ensure at least one of that type appears
    required = []
    if use_letters:
        letters_pool = ''.join(ch for ch in string.ascii_letters if ch not in exclude_chars)
        if letters_pool:
            required.append(secrets.choice(letters_pool))
    if use_numbers:
        digits_pool = ''.join(ch for ch in string.digits if ch not in exclude_chars)
        if digits_pool:
            required.append(secrets.choice(digits_pool))
    if use_symbols:
        symbols_pool = ''.join(ch for ch in string.punctuation if ch not in exclude_chars)
        if symbols_pool:
            required.append(secrets.choice(symbols_pool))

    if len(required) > length:
        raise ValueError("Length too small for selected rules. Increase length.")

    # Fill remaining characters
    password_chars = required[:]
    while len(password_chars) < length:
        password_chars.append(secrets.choice(pool))

    # Secure shuffle
    sr = secrets.SystemRandom()
    sr.shuffle(password_chars)

    return ''.join(password_chars)

def on_generate():
    try:
        length = int(length_var.get())
    except ValueError:
        messagebox.showerror("Oops", "Length must be a number.")
        return

    use_letters = letters_var.get() == 1
    use_numbers = numbers_var.get() == 1
    use_symbols = symbols_var.get() == 1
    exclude_chars = exclude_var.get()

    try:
        pwd = generate_secure_password(length, use_letters, use_numbers, use_symbols, exclude_chars)
        password_var.set(pwd)
    except ValueError as e:
        messagebox.showerror("Oops", str(e))

def on_copy():
    pwd = password_var.get()
    if not pwd:
        messagebox.showinfo("Info", "No password to copy.")
        return
    root.clipboard_clear()
    root.clipboard_append(pwd)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Build window
root = tk.Tk()
root.title("Random Password Generator")

# Length
tk.Label(root, text="Length:").grid(row=0, column=0, sticky="w", padx=8, pady=6)
length_var = tk.StringVar(value="12")
tk.Entry(root, textvariable=length_var, width=8).grid(row=0, column=1, padx=8, pady=6)

# Checkboxes
letters_var = tk.IntVar(value=1)
numbers_var = tk.IntVar(value=1)
symbols_var = tk.IntVar(value=1)

tk.Checkbutton(root, text="Letters (a–z, A–Z)", variable=letters_var).grid(row=1, column=0, columnspan=2, sticky="w", padx=8)
tk.Checkbutton(root, text="Numbers (0–9)", variable=numbers_var).grid(row=2, column=0, columnspan=2, sticky="w", padx=8)
tk.Checkbutton(root, text="Symbols (!@#$...)", variable=symbols_var).grid(row=3, column=0, columnspan=2, sticky="w", padx=8)

# Exclusions
tk.Label(root, text="Exclude characters (optional):").grid(row=4, column=0, sticky="w", padx=8, pady=6)
exclude_var = tk.StringVar(value="")
tk.Entry(root, textvariable=exclude_var, width=30).grid(row=4, column=1, padx=8, pady=6)

# Generate button
tk.Button(root, text="Generate", command=on_generate).grid(row=5, column=0, padx=8, pady=10)

# Password display
tk.Label(root, text="Password:").grid(row=6, column=0, sticky="w", padx=8)
password_var = tk.StringVar(value="")
pwd_entry = tk.Entry(root, textvariable=password_var, width=40)
pwd_entry.grid(row=6, column=1, padx=8, pady=6)
pwd_entry.configure(state="readonly")

# Copy button
tk.Button(root, text="Copy", command=on_copy).grid(row=7, column=0, padx=8, pady=10)

# Start app
root.mainloop()
