import random
import time

# "R" for "rock", "P" for "paper", "S" for "scissors"
game_list = ["R", "P", "S"]


# introduction function for the game
def intro():
    print('\nHello... welcome to Rock-Paper-Scissors game\n')
    time.sleep(2)
    print('\nHere, "R" for "rock", "P" for "paper", "S" for "scissors"')
    time.sleep(2)
    print("""\nThe game rules are as follows:
    If PLAYER and CPU choose the same “character” it’s a tie, and the game repeats
    Rock beats Scissors
    Paper beats Rock
    Scissors beats Paper
    """)
    time.sleep(2)

# the game function involving receiving player's input and conditionals
def game():
    intro() #  calling the intro function 
    
    while True: #  a while loop that repeats asking the player to insert a right or recognisable input
        # player choice of either rock paper or scissors
        player = input('Please enter a character... "R" or "P" or "S"\n').lower()
        # random choice for the CPU
        cpu = random.choice(game_list).lower()
        if player == "r" or player == "p" or player == "s":
            print(f"\nPLAYER ({player.upper()}) : CPU ({cpu.upper()})")
            break
        else:
            print("\nThe character you entered is not recognised\n")
    
    if player == "r" and cpu == "p":
        print("You chose 'Rock' , CPU chose 'Paper'")
        time.sleep(1)
        print("\nYou LOSE!!! PAPER beats ROCK")
        replay()
    elif player == "p" and cpu == "s":
        print("You chose 'Paper' , CPU chose 'Scissors'")
        time.sleep(1)
        print("\nYou LOSE!!! SCISSORS beats PAPER")
        replay()
    elif player == "s" and cpu == "r":
        print("\nYou chose 'Scissors' , CPU chose 'Rock'")
        time.sleep(1)
        print("\nYou LOSE!!! ROCK beats SCISSORS")
        replay()
    elif player == "r" and cpu == "s":
        print("You chose 'Rock' , CPU chose 'Scissors'")
        time.sleep(1)
        print("\nYou WIN!!! ROCK beats SCISSORS")
        replay_after_win()
    elif player == "s" and cpu == "p":
        print("You chose 'Scissors' , CPU chose 'Paper'")
        time.sleep(1)
        print("\nYou WIN!!! SCISSORS beats PAPER")
        replay_after_win()
    elif player == "p" and cpu == "r":
        print("You chose 'Paper' , CPU chose 'Rock'")
        time.sleep(1)
        print("\nYou WIN!!! PAPER beats ROCK")
        replay_after_win()
    elif player == "r" and cpu == "r":
        print("You chose 'Rock' , CPU chose 'Rock'")
        auto_restart()
    elif player == "s" and cpu =="s":
        print("You chose 'Scissors' , CPU chose 'Scissors'")
        auto_restart()
    elif player == "p" and cpu == "p":
        print("You chose 'Paper' , CPU chose 'Paper'")
        auto_restart()


# function that asks user if they would like to replay the game after losing
def replay():
    play_again = input("\nWill you like to play again? Enter yes or no\n").lower()
    if play_again == "yes":
        game()
    elif play_again == "no":
        print("Thank you for playing the game, better luck next time")
    else:
        replay()


# function that asks user if they would like to replay the game after winning
def replay_after_win():
    play_again = input("Will you like to play again? Enter yes or no\n").lower()
    if play_again == "yes":
        game()
    elif play_again == "no":
        print("Thank you for playing the game, CONGRATULATIONS on your win!!!")
    else:
        replay_after_win()


# function that automatically restarts the game if it is a tie
def auto_restart():
        time.sleep(1)
        print("That is a tie, DRAW!!! we restart the game")
        time.sleep(3)
        game()
        

# function that calls the game to run
game()
