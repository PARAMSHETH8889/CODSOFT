import random
import tkinter as tk

# Define the options and scores
options = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

# Define the functions for the game
def play(player_choice):
    global player_score, computer_score
    computer_choice = random.choice(options)
    if player_choice == computer_choice:
        result_label.config(text="Tie!")
    elif player_choice == "rock" and computer_choice == "scissors" or player_choice == "paper" and computer_choice == "rock" or player_choice == "scissors" and computer_choice == "paper":
        player_score += 1
        result_label.config(text="You win!")
    else:
        computer_score += 1
        result_label.config(text="Computer wins!")
    score_label.config(text="Player: {}  Computer: {}".format(player_score, computer_score))

def play_again():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    score_label.config(text="Player: {}  Computer: {}".format(player_score, computer_score))
    result_label.config(text="")
    
# Create the GUI
root = tk.Tk()
root.title("Rock, Paper, Scissors")

rock_button = tk.Button(root, text="Rock", command=lambda: play("rock"))
rock_button.pack(side=tk.LEFT, padx=10)

paper_button = tk.Button(root, text="Paper", command=lambda: play("paper"))
paper_button.pack(side=tk.LEFT, padx=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play("scissors"))
scissors_button.pack(side=tk.LEFT, padx=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Player: 0  Computer: 0")
score_label.pack()

play_again_button = tk.Button(root, text="Play Again", command=play_again)
play_again_button.pack(pady=10)

root.mainloop()