import tkinter as tk
from tkinter import messagebox
import random

def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return None
    if (player1_choice == 'rock' and player2_choice == 'scissors') or \
       (player1_choice == 'scissors' and player2_choice == 'paper') or \
       (player1_choice == 'paper' and player2_choice == 'rock'):
        return "Player 1"
    else:
        return "Player 2"

def play_game():
    player1_choice = player1_var.get()
    player2_choice = player2_var.get()

    winner = determine_winner(player1_choice, player2_choice)
    if winner:
        messagebox.showinfo("Result", f"{winner} wins!")
    else:
        messagebox.showinfo("Result", "It's a tie!")

def reset_choices():
    player1_var.set("")
    player2_var.set("")

root = tk.Tk()
root.title("Rock Paper Scissors")

choices = ['rock', 'paper', 'scissors']

player1_label = tk.Label(root, text="Player 1:")
player1_label.grid(row=0, column=0, padx=10, pady=5)
player1_var = tk.StringVar()
player1_entry = tk.Entry(root, textvariable=player1_var)
player1_entry.grid(row=0, column=1, padx=10, pady=5)

player2_label = tk.Label(root, text="Player 2:")
player2_label.grid(row=1, column=0, padx=10, pady=5)
player2_var = tk.StringVar()
player2_entry = tk.Entry(root, textvariable=player2_var)
player2_entry.grid(row=1, column=1, padx=10, pady=5)

play_button = tk.Button(root, text="Play", command=play_game)
play_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="we")

reset_button = tk.Button(root, text="Reset", command=reset_choices)
reset_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="we")

root.mainloop()
