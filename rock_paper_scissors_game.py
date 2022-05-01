"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""


import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    """Class for player that always returns a random move"""
    def move(self):
        my_move = random.choice(moves)
        return my_move


class HumanPlayer(Player):
    """Class to represent human players"""
    def __init__(self):
        self.choice = ""
        self.choices = ['rock', 'paper', 'scissors', 'quit']

    def move(self):
        self.choice = ""
        while self.choice not in self.choices:
            self.choice = input("rock, paper, scissors? > ").lower()
        return self.choice


class ReflectPlayer(Player):
    """Computer player that repeats the oponents previous move,
       should lead with random to keep mirror matches from always tying"""
    def __init__(self):
        self.next_move = random.choice(moves)

    def move(self):
        return self.next_move

    def learn(self, my_move, their_move):
        self.next_move = their_move


class CyclePlayer(ReflectPlayer):
    """Computer player that cycles through moves after an initial
       random move"""

    def learn(self, my_move, their_move):
        self.next_move = moves[(moves.index(my_move) + 1) % 3]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score = {
            "p1": 0,
            "p2": 0,
            "ties": 0
        }
        self.game_round = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        if move1 == 'quit':
            self.end_game()
        elif move1 == move2:
            self.score["ties"] += 1
        elif beats(move1, move2):
            self.score["p1"] += 1
        elif beats(move2, move1):
            self.score["p2"] += 1
        else:
            print("Invalid round!")

        print(f"Player 1: {move1}  Player 2: {move2}")
        print(f"Score: Player 1: {self.score['p1']}   ****   "
              f"Player 2: {self.score['p2']}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Rock Paper Scissors, start!\n(Type 'quit' to end)")
        # for game_round in range(3):
        while True:
            self.game_round += 1
            print(f"Round {self.game_round}:")
            self.play_round()

    def end_game(self):
        print("Game over!")
        print(f"Player 1 won {self.score['p1']} times")
        print(f"Player 2 won {self.score['p2']} times")
        print(f"And {self.score['ties']} ties")
        if self.score['p1'] == self.score['p2']:
            print('**The game is a tie!**')
        elif self.score['p1'] > self.score['p2']:
            print('**You WIN!**')
        else:
            print('**The computer won, this time...**')
        quit()


if __name__ == '__main__':
    computer_player = random.choice([CyclePlayer(), RandomPlayer(),
                                     ReflectPlayer()])
    # should I have it randomize per round perhaps?
    game = Game(HumanPlayer(), computer_player)
    game.play_game()
