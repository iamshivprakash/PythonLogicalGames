import random
from random import randint
from art import logo
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5

# ...........................My attempt..................................
# number_list = []
# for number in range(1,101):
#     number_list.append(number)
# # print(number_list)
# guessed_number=random.choice(number_list)
# # print(guessed_number)
#
# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 amd 100.")
# level=input("Choose a difficulty. Type 'easy' or 'hard':")
#
# if level=='hard':
#     attempts=5
# else:
#     attempts=10
# is_number_guessed = False
# while not is_number_guessed:
#     if attempts == 0:
#         is_number_guessed = True
#         print("You have no more attempts.")
#     else:
#         print(f"you have {attempts} attempts to guess the number:")
#         user_guess = int(input("your guess: "))
#         if user_guess == guessed_number:
#             is_number_guessed = True
#             print("You get it right.")
#         elif user_guess > guessed_number:
#             attempts -= 1
#             print("Too high")
#         elif user_guess < guessed_number:
#             attempts -= 1
#             print("Too low")



# .......................Instructor Solution....................
def check_answer(guess, answer,turns):
    if guess>answer:
        print("Too high")
        return turns-1
    elif guess<answer:
        print("Too low")
        return turns-1
    else:
        print(f"You get it right! The answer was {answer}")
def set_difficulty():
    level=input("Choose a difficulty. Type 'easy' or 'hard':")
    if level=='easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 amd 100.")
    answer = randint(1,100)

    turns = set_difficulty()

    guess=0
    while guess!=answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns=check_answer(guess,answer,turns)
        if turns==0:
            print("you've run out of guesses, you lose.")
            return
        elif turns!=0:
            print("Guess again.")

game()