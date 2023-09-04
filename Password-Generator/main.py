import random
import string
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox

def generate_password(length, strength):
    characters = ""

    if strength == "Weak":
        characters = string.ascii_letters + string.digits
    elif strength == "Medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif strength == "Strong":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase
    else:
        raise ValueError("Invalid strength level. Choose 'Weak', 'Medium', or 'Strong'.")

    if not characters:
        raise ValueError("Invalid strength level. Choose 'Weak', 'Medium', or 'Strong'.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_callback():
    try:
        password_length = int(length_entry.get())
        if password_length <= 0:
            raise ValueError("Password length must be a positive integer.")

        strength = strength_combobox.get()
        password = generate_password(password_length, strength)
        result_label.config(text=f"Generated password: {password}")

        generate_button.config(state=tk.DISABLED)
        generate_another_button.config(state=tk.NORMAL)
        save_button.config(state=tk.NORMAL)

        global current_password
        current_password = password
    except ValueError as e:
        result_label.config(text=f"Error: {e}")

def generate_another_password_callback():
    generate_password_callback()  # Call generate_password_callback to generate a new password

def save_password_callback():
    try:
        service_name = simpledialog.askstring("Service Name", "Enter the service or website name:")
        if service_name:
            save_password(service_name, current_password)
            messagebox.showinfo("Password Saved", "Password saved successfully.")
        else:
            messagebox.showwarning("Password Not Saved", "Service name is required to save the password.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the password: {str(e)}")

def save_password(service_name, password):
    with open("passwords.txt", "a") as file:
        file.write(f"Service: {service_name}, Password: {password}\n")

# Create the main application window
root = tk.Tk()
root.title("Password Generator")

# Create and configure widgets
style = ttk.Style()
style.configure("TButton", foreground="black", background="blue", padding=5)
style.configure("TLabel", foreground="black", background="white", padding=5)

length_label = ttk.Label(root, text="Enter the desired length of the password:")
length_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")

length_entry = ttk.Entry(root)
length_entry.grid(row=0, column=2, padx=10, pady=10, sticky="w")

strength_label = ttk.Label(root, text="Choose password strength:")
strength_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="w")

strength_combobox = ttk.Combobox(root, values=["Weak", "Medium", "Strong"])
strength_combobox.grid(row=1, column=2, padx=10, pady=10, sticky="w")
strength_combobox.set("Weak")

generate_button = ttk.Button(root, text="Generate Password", command=generate_password_callback, style="TButton")
generate_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

generate_another_button = ttk.Button(root, text="Generate Another Password", command=generate_another_password_callback, style="TButton", state=tk.DISABLED)
generate_another_button.grid(row=2, column=1, padx=10, pady=10, sticky="w")

save_button = ttk.Button(root, text="Save Password", command=save_password_callback, style="TButton", state=tk.DISABLED)
save_button.grid(row=2, column=2, padx=10, pady=10, sticky="w")

result_label = ttk.Label(root, text="", style="TLabel")
result_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="w")

# Store the current generated password
current_password = ""

# Start the GUI event loop
root.mainloop()
