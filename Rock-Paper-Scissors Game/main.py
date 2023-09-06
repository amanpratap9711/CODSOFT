import tkinter as tk
import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_choice = user_choice_var.get()
    computer_choice = get_computer_choice()

    user_choice_label.config(text=f"You chose: {user_choice}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Result: {result}")

def reset_game():
    user_choice_var.set("rock")
    user_choice_label.config(text="")
    computer_choice_label.config(text="")
    result_label.config(text="")

# Create the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors")

# Set the background color and window size
window.configure(bg='#C4E4B7')
window.geometry("400x400")

# Label for user and computer choices
user_choice_label = tk.Label(window, text="", font=("Helvetica", 16), bg='#C4E4B7')
computer_choice_label = tk.Label(window, text="", font=("Helvetica", 16), bg='#C4E4B7')
user_choice_label.pack()
computer_choice_label.pack()

# Label for the result
result_label = tk.Label(window, text="", font=("Helvetica", 16), bg='#C4E4B7')
result_label.pack()

# Radio buttons for user choice
user_choice_var = tk.StringVar()
user_choice_var.set("rock")
rock_radio = tk.Radiobutton(window, text="Rock", variable=user_choice_var, value="rock", bg='#C4E4B7')
paper_radio = tk.Radiobutton(window, text="Paper", variable=user_choice_var, value="paper", bg='#C4E4B7')
scissors_radio = tk.Radiobutton(window, text="Scissors", variable=user_choice_var, value="scissors", bg='#C4E4B7')
rock_radio.pack()
paper_radio.pack()
scissors_radio.pack()

# Play and Reset buttons
play_button = tk.Button(window, text="Play", command=play_game, bg='#6CBB63', fg='white', font=("Helvetica", 16))
reset_button = tk.Button(window, text="Reset", command=reset_game, bg='#FF6B6B', fg='white', font=("Helvetica", 16))
play_button.pack(pady=10)
reset_button.pack()

# Start the GUI
window.mainloop()
