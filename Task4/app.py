import tkinter as tk
import random
from tkinter import messagebox

# Initialize scores
user_score = 0
computer_score = 0

# Function to reset scores
def reset_scores():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    update_scoreboard()

# Function to update the scoreboard
def update_scoreboard():
    score_label.config(text=f"User: {user_score}  |  Computer: {computer_score}")

# Function to generate computer's choice
def computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

# Function to play a round
def play_round(user_choice):
    global user_score, computer_score
    comp_choice = computer_choice()
    
    # Determine the winner
    if user_choice == comp_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Scissors" and comp_choice == "Paper") or \
         (user_choice == "Paper" and comp_choice == "Rock"):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    # Update the result display
    result_label.config(text=f"User chose: {user_choice}\nComputer chose: {comp_choice}\n\n{result}")
    update_scoreboard()

# GUI setup
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("400x400")

# Label for title
title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 16))
title_label.pack(pady=10)

# Buttons for user choice
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play_round("Rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play_round("Paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play_round("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)

# Label for showing the result of each round
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Scoreboard
score_label = tk.Label(root, text="User: 0  |  Computer: 0", font=("Arial", 12))
score_label.pack(pady=10)

# Reset button
reset_button = tk.Button(root, text="Reset Scores", command=reset_scores)
reset_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
