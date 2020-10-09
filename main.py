import random

OPTIONS = ['rock', 'paper', 'scissors']


def get_computer_choice():
    return random.choice(OPTIONS)


def get_human_choice():
    choice_number = int(input("Enter the number of your choice: "))
    return OPTIONS[choice_number - 1]


def print_options():
    print("\n".join(f"({i}) {option.title()}" for i, option in enumerate(OPTIONS)))


def print_choices(human_choice, computer_choice):
    print(f"You chose: {human_choice}")
    print(f"Computer chose: {computer_choice}")


def print_win_loose(human_choice, computer_choice, human_beats, human_loses_to):
    if computer_choice == human_beats:
        print(f"Sorry, {computer_choice} beats {human_choice}")
    elif computer_choice == human_loses_to:
        print(f"Yes, {human_choice} beats {computer_choice}")


def print_result(human_choice, computer_choice):
    if human_choice == computer_choice:
        print("Draw!")
    if human_choice == "rock":
        print_win_loose("rock", computer_choice, "scissors", "paper")
    elif human_choice == "scissors":
        print_win_loose("scissors", computer_choice, "paper", "rock")
    elif human_choice == "paper":
        print_win_loose("paper", computer_choice, "rock", "scissors")


print_options()
human_choice = get_human_choice()
computer_choice = get_computer_choice()
print_choices(human_choice, computer_choice)
print_result(human_choice, computer_choice)
