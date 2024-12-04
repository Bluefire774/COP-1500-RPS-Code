import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.player_score = 0
        self.computer_score = 0
        self.round_number = 1
    def round_winner(self, player, computer):
        if player == computer:
            return "tie"
        elif (player == "rock" and computer == "scissors") or \
            (player == "paper" and computer == "rock") or \
            (player == "scissors" and computer == "paper"):
            return "player"
        else:
            return "computer"
    def play_round(self):
        print(f"Round {self.round_number}")
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if player_choice not in self.choices:
            print("Invalid choice. Please enter rock, paper, or scissors")
            return
        computer_choice = random.choice(self.choices)
        print(f"Computer chose {computer_choice}\n")

        winner = self.round_winner(player_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "player":
            print("Player wins!")
            self.player_score += 1
        elif winner == "computer":
            print("Computer wins!")
            self.computer_score += 1
        print(f"Score: Player {self.player_score} - Computer {self.computer_score}\n")
        self.round_number += 1

    def play_game(self):
        print("Rock, Paper, Scissors Match\n")

        while self.player_score < 3 and self.computer_score < 3:
            self.play_round()

        if self.player_score > self.computer_score:
            print("Player wins the match!")

        else:
            print("Computer wins the match!")

game = RockPaperScissors()
game.play_game()