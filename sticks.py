"""
Suggested Development Process

Decide on the data structure(s) that you are going to need to use to represent the state of the game when played.



Decide on the tasks that will be part of the game loop.
Write test function(s) for a single task.
Write function(s) for the task and make sure your test(s) pass.
Repeat steps 3 and 4 until all tasks are implemented.
Write a main() function with a game loop that uses your already tested and developed functionality in conjunction with getting user input and printing StickGameut.

"""
import random

class StickGame:
    """Creates new instance of a StickGame """
    def setup(self):
        while True:
            try:
                sticks = int(input("How many sticks are on the table initially (10-100)? "))
            except ValueError:
                print("Please enter an integer between 10 and 100.")
                continue
            if sticks < 10 or sticks > 100:
                print("Please enter an integer between 10 and 100.")
                continue
            else:
                self.sticks = sticks
                break

        self.player_turn = "Player 1"


    def take_sticks(self):
        """The current player takes sticks. """
        print("\nThere are {} sticks on the board".format(self.sticks))
        while True:
            try:
                sticks_taken = int(input("{} How many sticks do you take (1-3)? ".format(self.player_turn)))
            except ValueError:
                print("Please enter an integer between 1 and 3.")
                continue
            if sticks_taken < 1 or sticks_taken > 3:
                print("Please enter an integer between 1 and 3.")
                continue
            else:
                self.sticks -= sticks_taken
                break

    def take_sticks_like_a_pro(self):
        print("\nThere are {} sticks on the board".format(self.sticks))
        shit_sticks = 1
        while shit_sticks < self.sticks - 4:
            shit_sticks += 4
        if self.sticks - shit_sticks <= 3:
            sticks_taken = self.sticks - shit_sticks
        else:
            sticks_taken = 1
        self.sticks -= sticks_taken
        print("Player 2 (Smart AI) takes {} sticks".format(sticks_taken))

    def change_turn(self):
        if self.player_turn == "Player 1":
            self.player_turn = "Player 2"
        elif self.player_turn == "Player 2":
            self.player_turn = "Player 1"

    def __init__(self):
        print("Welcome to the Game of Sticks!")
        mode = input("""'P' for Player vs. Player
'S' for Player vs. Smart AI
'A' for AI vs. AI
'Any Other Key' for Player vs. Slow Learning AI""").lower()
        if mode == 'p':
            print("You've selected Player vs. Player!")
            self.mode = 'human'
        elif mode == 's':
            print("You've selected Player vs. Smart AI!")
            self.mode = 'no fun'
        elif mode == 'a':
            print("You've selected Player vs. Smart AI!")
            self.mode = 'ai ai'
        else:
            print("You've selected Player vs. Learning Slowly AI!")
            self.mode = 'ai'

        while True:
            try:
                sticks = int(input("How many sticks are on the table initially (10-100)? "))
            except ValueError:
                print("Please enter an integer between 10 and 100.")
                continue
            if sticks < 4 or sticks > 100:
                print("Please enter an integer between 10 and 100.")
                continue
            else:
                self.start_sticks = sticks
                self.sticks = sticks
                break

        if self.mode == 'ai':
            self.ai = AI(self.sticks)
        elif self.mode == 'ai ai':
            self.ai1 = AI(self.sticks)
            self.ai2 = AI(self.sticks)

        while True:
            self.sticks = self.start_sticks
            self.player_turn = "Player 1"
            while self.sticks > 0:
                if self.mode == 'ai' and self.player_turn == "Player 2":
                    self.ai.take_sticks_ai(self.sticks)
                    self.change_turn()
                elif self.mode == 'no fun' and self.player_turn == "Player 2":
                    self.take_sticks_like_a_pro()
                    self.change_turn()
                elif self.mode == 'ai ai' and self.player_turn == "Player 1":
                    self.ai1.take_sticks_ai(self.sticks)
                    self.change_turn()
                elif self.mode == 'ai ai' and self.player_turn == "Player 2":
                    self.ai2.take_sticks_ai(self.sticks)
                    self.change_turn()
                else:
                    self.take_sticks()
                    self.change_turn()
            print("{} wins!".format(self.player_turn))

            replay = input("'Y' to play again, Any Key to quit: ").lower()

            if replay != 'y':
                if self.mode == 'ai':
                    print(self.ai)
                elif self.mode == 'ai ai':
                    print("Player 1 AI")
                    print(self.ai1)
                    print("Player 2 AI")
                    print(self.ai2)

                print("Thanks for playing!")
                break

class AI:
    def __init__(self, sticks):
        self.hats = {}
        self.sticks = sticks
        for i in range(1, self.sticks + 1):
            self.hats[i] = {'content': [1,2,3], 'choice': None}

    def __str__(self):
        for keys, values in self.hats.items():
            print("{}: {}".format(keys, values))
        return __name__

    def take_sticks_ai(self, sticks):
        """Choose a random number of sticks from the hat content,
           and record the choice"""
        print("\nThere are {} sticks on the board".format(sticks))
        sticks_taken = random.choice(self.hats[sticks]['content'])
        self.hats[sticks]['choice'] = sticks_taken
        sticks -= sticks_taken
        return sticks

def main():
    StickGame()


"""
Welcome to the Game of Sticks!
How many sticks are there on the table initially (10-100)? 500
Please enter a number between 10 and 100.
How many sticks are there on the table initially (10-100)? 3
Please enter a number between 10 and 100.
How many sticks are there on the table initially (10-100)? 50

There are 50 sticks on the board.
Player 1: How many sticks do you take (1-3)? 3

There are 47 sticks on the board.
Player 2: How many sticks do you take (1-3)? 55
Please enter a number between 1 and 3
Player 2: How many sticks do you take (1-3)? 3

There are 44 sticks on the board.
Player 1: How many sticks do you take (1-3)? 3
...

There is 1 stick on the board.
Player 1: How many sticks do you take (1-3)? 1
Player 1, you lose.
"""

"""
Welcome to the Game of Sticks!
How many sticks are there on the table initially (10-100)? 10
Options:
 Play against a friend (1)
 Play against the computer (2)
 Play against the trained computer (3)
Which option do you take (1-3)? 3
Training AI, please wait...

There are 10 sticks on the board.
Player 1: How many sticks do you take (1-3)? 3

There are 7 sticks on the board.
AI selects 2.

There are 5 sticks on the board.
Player 1: How many sticks do you take (1-3)? 1

There are 4 sticks on the board.
AI selects 3.

There is 1 stick on the board.
Player 1: How many sticks do you take (1-3)? 1
You lose.
Play again (y/n)? y

There are 10 sticks on the board.
Player 1: How many sticks do you take (1-3)? 2

There are 8 sticks on the board.
AI selects 3.

There are 5 sticks on the board.
Player 1: How many sticks do you take (1-3)? 2

There are 3 sticks on the board.
AI selects 2.

There is 1 stick on the board.
Player 1: How many sticks do you take (1-3)? 1
You lose.
Play again (y/n)? n

"""


if __name__ == '__main__':
    main()

"""
    def take_sticks_ai(self):
        #Choose a random number of sticks from the hat content,
        #and record the choice
        sticks_taken = random.choice(self.ai.hats[self.sticks]['content'])
        self.ai.hats[self.sticks]['choice'] = sticks_taken
        self.sticks -= sticks_taken

"""
