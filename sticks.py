"""
Suggested Development Process

Decide on the data structure(s) that you are going to need to use to represent the state of the game when played.



Decide on the tasks that will be part of the game loop.
Write test function(s) for a single task.
Write function(s) for the task and make sure your test(s) pass.
Repeat steps 3 and 4 until all tasks are implemented.
Write a main() function with a game loop that uses your already tested and developed functionality in conjunction with getting user input and printing StickGameut.

"""

class StickGame:
    """Creates new instance of a StickGame """
    def setup(self):
        print("Welcome to the Game of Sticks!")
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
                self.sticks_taken = sticks_taken
                break

        self.sticks -= self.sticks_taken

    def change_turn(self):
        if self.player_turn == "Player 1":
            self.player_turn = "Player 2"
        elif self.player_turn == "Player 2":
            self.player_turn = "Player 1"





    def __init__(self):
        self.setup()
        while self.sticks > 0:
            self.take_sticks()
            self.change_turn()
        print("{} wins!".format(self.player_turn))






def main():
    stick_game = StickGame()

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

if __name__ == '__main__':
    main()
