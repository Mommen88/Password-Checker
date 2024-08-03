import re
import tkinter as tk
from tkinter import messagebox

def password_complexity_checker(password):
    score = 0

    # Check password length
    if len(password) < 8:
        score -= 20
    elif len(password) < 12:
        score += 10
    else:
        score += 20

    # Check for character distribution
    has_uppercase = re.search(r"[A-Z]", password) is not None
    has_lowercase = re.search(r"[a-z]", password) is not None
    has_numbers = re.search(r"\d", password) is not None
    has_special_chars = re.search(r"[^a-zA-Z0-9]", password) is not None

    if has_uppercase:
        score += 10
    if has_lowercase:
        score += 10
    if has_numbers:
        score += 10
    if has_special_chars:
        score += 10

    # Check for common patterns or sequences
    has_sequence = False
    for i in range(len(password) - 2):
        if ord(password[i]) == ord(password[i + 1]) - 1 and ord(password[i + 1]) == ord(password[i + 2]) - 1:
            has_sequence = True
            break
    if has_sequence:
        score -= 10

    # Analyze password strength
    password_length = len(password)

    # Return password complexity rating and detailed feedback
    if score < 20:
        return "Very Weak", f"Password is very weak because it is too short ({password_length} characters) and lacks variety in character distribution (uppercase: {has_uppercase}, lowercase: {has_lowercase}, numbers: {has_numbers}, special characters: {has_special_chars}). It also contains a common sequence. Consider adding more characters and special characters."
    elif score < 40:
        return "Weak", f"Password is weak because it lacks variety in character distribution (uppercase: {has_uppercase}, lowercase: {has_lowercase}, numbers: {has_numbers}, special characters: {has_special_chars}). It also contains a common sequence. Try adding more special characters and increasing the password length."
    elif score < 60:
        return "Medium", f"Password is medium strength because it has a good length ({password_length} characters) and variety in character distribution (uppercase: {has_uppercase}, lowercase: {has_lowercase}, numbers: {has_numbers}, special characters: {has_special_chars}). However, it contains a common sequence. Consider adding more special characters and avoiding common patterns."
    elif score < 80:
        return "Strong", f"Password is strong because it has a good length ({password_length} characters) and variety in character distribution (uppercase: {has_uppercase}, lowercase: {has_lowercase}, numbers: {has_numbers}, special characters: {has_special_chars})."
    else:
        return "Very Strong", f"Password is very strong because it has a good length ({password_length} characters) and variety in character distribution (uppercase: {has_uppercase}, lowercase: {has_lowercase}, numbers: {has_numbers}, special characters: {has_special_chars}). It also does not contain any common sequences or similarities to previously used passwords."

def check_password():
    password = password_entry.get()
    if password:
        strength, feedback = password_complexity_checker(password)
        result_label.config(text=f"Password complexity: {strength}\n\nFeedback: {feedback}")
    else:
        messagebox.showwarning("Input Error", "Please enter a password.")

# Create the main application window
app = tk.Tk()
app.title("Password Complexity Checker")

# Add a label and entry for password input
password_label = tk.Label(app, text="Enter a password:")
password_label.pack(pady=5)
password_entry = tk.Entry(app, show="*", width=30)
password_entry.pack(pady=5)

# Add a button to check password complexity
check_button = tk.Button(app, text="Check Password", command=check_password)
check_button.pack(pady=10)

# Add a label to display the result
result_label = tk.Label(app, text="", wraplength=300)
result_label.pack(pady=10)

# Run the application
app.mainloop()
