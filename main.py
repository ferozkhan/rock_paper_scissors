import random

OPTIONS = ['rock', 'paper', 'scissors']


class RockPaperScissorsSimulator:

    def __init__(self):
        self.computer_choice = None
        self.human_choice = None
        self.computer = None

    def get_computer_choice(self):
        self.computer_choice = random.choice(OPTIONS)

    def get_human_choice(self):
        choice_number = int(input("Enter the number of your choice: "))
        self.human_choice = OPTIONS[choice_number - 1]

    @staticmethod
    def print_options():
        print("\n".join(f"({i}) {option.title()}" for i, option in enumerate(OPTIONS)))

    def print_choices(self):
        print(f"You chose:      {self.human_choice.title()}")
        print(f"Computer chose: {self.computer_choice.title()}")

    def print_win_loose(self, human_beats, human_loses_to):
        if self.computer_choice == human_beats:
            print(f"Sorry, {self.computer_choice} beats {self.human_choice}")
        elif self.computer_choice == human_loses_to:
            print(f"Yes, {self.human_choice} beats {self.computer_choice}")

    def print_result(self):
        if self.human_choice == self.computer_choice:
            print("Draw!")
        if self.human_choice == "rock":
            self.print_win_loose("scissors", "paper")
        elif self.human_choice == "scissors":
            self.print_win_loose("paper", "rock")
        elif self.human_choice == "paper":
            self.print_win_loose("rock", "scissors")

    def simulate(self):
        self.print_options()
        self.get_human_choice()
        self.get_computer_choice()
        self.print_choices()
        self.print_result()


simulator = RockPaperScissorsSimulator()
simulator.simulate()
