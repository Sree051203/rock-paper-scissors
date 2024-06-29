#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
from collections import defaultdict

moves = ['rock', 'paper', 'scissors']

def determine_winner(player_move, computer_move):
    if player_move == computer_move:
        return 'draw'
    elif (player_move == 'rock' and computer_move == 'scissors') or          (player_move == 'scissors' and computer_move == 'paper') or          (player_move == 'paper' and computer_move == 'rock'):
        return 'player'
    else:
        return 'computer'

def predict_next_move(player_history):
    if not player_history:
        return random.choice(moves)
    
    move_counts = defaultdict(int)
    for move in player_history:
        move_counts[move] += 1

    most_common_move = max(move_counts, key=move_counts.get)
    
    if most_common_move == 'rock':
        return 'paper' 
    elif most_common_move == 'paper':
        return 'scissors' 
    else:
        return 'rock' 

def play_game():
    player_history = []
    computer_score = 0
    player_score = 0
    rounds = 10

    print("Let's play Rock-Paper-Scissors!")
    print("Enter 'rock', 'paper', or 'scissors' to play. Enter 'quit' to stop playing.")

    for _ in range(rounds):
        player_move = input("Your move: ").lower()
        if player_move == 'quit':
            break
        if player_move not in moves:
            print("Invalid move. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        computer_move = predict_next_move(player_history)
        player_history.append(player_move)

        print(f"Computer move: {computer_move}")
        winner = determine_winner(player_move, computer_move)

        if winner == 'player':
            player_score += 1
            print("You win this round!")
        elif winner == 'computer':
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a draw!")

        print(f"Score - You: {player_score}, Computer: {computer_score}\n")

    print("Game over!")
    print(f"Final Score - You: {player_score}, Computer: {computer_score}")

if __name__ == "__main__":
    play_game()


# In[ ]:




