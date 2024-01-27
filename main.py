from visualizations import *
import random

class RockPaperScissorsGame:
    def __init__(self):
        # Initialize scores for the player and the computer
        self.score_player = 0
        self.score_computer = 0

    def draw_visuals(self, x):
        """
        Returns the visual representation of the player's choice.

        Args:
        - x (int): Player's choice (1 for Rock, 2 for Paper, 3 for Scissors).

        Returns:
        - str: Visual representation of the player's choice.
        """
        if x == 1:
            return rock
        elif x == 2:
            return paper
        elif x == 3:
            return scissors
        else:
            return 'Wrong choice'

    def print_result(self, player, computer):
        """
        Prints the result of the round and updates the scores.

        Args:
        - player (int): Player's choice (1 for Rock, 2 for Paper, 3 for Scissors).
        - computer (int): Computer's randomly generated choice.
        """
        print(f"Computer chose:\n{self.draw_visuals(computer)}")

        if player == computer:
            print("Draw")
        elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
            print("You win")
            self.score_player += 1
        else:
            print("You lose")
            self.score_computer += 1

        print(f"Your score: {self.score_player}\nComputer score: {self.score_computer}")

    def play_round(self, user_input):
        """
        Plays a round of Rock-Paper-Scissors.

        Args:
        - user_input (int): Player's choice (1 for Rock, 2 for Paper, 3 for Scissors).
        """
        try:
            # Convert user input to integer
            user_input = int(user_input)

            # Check if user input is within the valid range (1 to 3)
            if 1 <= user_input <= 3:
                computer_choice = random.randint(1, 3)
                print(self.draw_visuals(user_input))
                self.print_result(user_input, computer_choice)
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    # Create an instance of the RockPaperScissorsGame class
    game = RockPaperScissorsGame()

    while game.score_player < 10 and game.score_computer < 10:
        # Get user input for the player's choice
        user_input = input("What do you choose? Type 1 for Rock, 2 for Paper, or 3 for Scissors.\n")
        # Play a round of the game
        game.play_round(user_input)

    # Check the winner and display a message
    if game.score_player >= 10:
        print("Congratulations! You won the game!")
    else:
        print("Good luck next time! You lost the game.")
