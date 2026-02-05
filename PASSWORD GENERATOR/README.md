🔐 Random Password Generator

A Python project that generates secure, customizable random passwords.  
It includes both a **command-line version** (for beginners) and a **GUI version** (for advanced users).

✨ Features

# Beginner (Command-Line)
- Generate random passwords with user-defined length.
- Choose character types: letters, numbers, symbols.
- Input validation (positive length, at least one character type).
- Ensures strong randomness using Python’s `secrets` module.

# Advanced (GUI with Tkinter)
- User-friendly graphical interface.
- Options for password length, character types, and exclusions.
- Security rules: guarantees at least one of each selected type.
- Clipboard integration: copy generated password with one click.
- Customization: exclude specific characters (e.g., `O0l1`).
- Error handling with helpful pop-up messages.

## 🛠️ Requirements

- Python 3.8+
- Tkinter (comes pre-installed with Python)
- No external libraries required.

## 🚀 How to Run

### Command-Line Version
1. Open terminal in the project folder.
2. Run:
   ```bash
   python random_password_generator.py
3.Follow the prompts to generate a password.

# GUI Version:
Open terminal in the project folder.

Run:

bash
python gui_password_generator.py
Use the window to set options, generate, and copy passwords.

📸 Screenshots

Command-Line: Prompts for length and character types.
GUI: Window with length field, checkboxes, exclude box, generate and copy buttons.

✅ Project Checklist

[x] Randomization
[x] User input validation
[x] Character set handling
[x] GUI design
[x] Security rules
[x] Clipboard integration
[x] Customization

📂 Project Structure

PASSWORD GENERATOR/
│
├── random_password_generator.py   # Beginner version
├── gui_password_generator.py      # Advanced GUI version
└── README.md                     # Project documentation

🔮 Future Improvements

~Add a “Save to file” option.
~Generate multiple passwords at once.
~Dark mode for GUI.
~Password strength meter.
