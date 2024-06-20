import random
import tkinter as tk

def generate_password():
    password_length = int(length_entry.get())
    generated_password = ""
    for _ in range(password_length):
        generated_password += chr(random.randint(49, 122))
    password_label.config(text=f"Generated password: {generated_password}")

window = tk.Tk()
window.title("Password Generator")

length_label = tk.Label(window, text="Enter length of password to generate:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = tk.Label(window, text="Required password will appear here")
password_label.pack()

window.mainloop()