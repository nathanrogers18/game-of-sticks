import random

class StickGame:
    def __init__(self, sticks, player_1_name, player_2_name):
        self.sticks = sticks
        self.turns = {player_1_name: player_2_name, player_2_name: player_1_name}
        self.turn = player_1_name
        self.sticks_taken = 0

    def person_turn(self):
        while True:
            try:
                self.sticks_taken = int(input("{} How many sticks do you take (1-3)? ".format(self.turn)))
            except ValueError:
                print("Please enter an integer between 1 and 3.")
                continue
            if self.sticks_taken < 1 or self.sticks_taken > 3:
                print("Please enter an integer between 1 and 3.")

    def ai_turn(self, ai):
        self.sticks_taken = random.choice(ai.hats[self.sticks]['content'])
        ai.hats[self.sticks]['choice'] = self.sticks_taken

    def smart_ai_turn(self):
        shit_sticks = 1
        while shit_sticks < self.sticks - 4:
            shit_sticks += 4
        if self.sticks - shit_sticks <= 3:
            self.sticks_taken = self.sticks - shit_sticks
        else:
            self.sticks_taken = 1




class PersonVPerson(StickGame):
    def __init__(self, sticks, turns, turn, sticks):
        super().__init__(sticks)


class PersonVAI(StickGame):
    def __init__(self, sticks):
        super().__init__(sticks)

class PersonVSmartAI(StickGame):
    def __init__(self, sticks):
        super().__init__(sticks)

class AIVAI(StickGame):
    def __init__(self, sticks):
        super().__init__(sticks)

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


def main():

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
            break

    print("Welcome to the Game of Sticks!")
    mode = input("""'1' for Person vs. Person
'2' for Player vs. Slow Machine Learning AI
'3' for Player vs. Smart AI
'Any Key' for AI vs. AI
""")
    if mode == 1:
        print("You've selected Player vs. Player!")
        game = PersonVPerson(sticks)
    elif mode == 2:
        print("You've selected Player vs. Slow Machine Learning AI!")
        game = PersonVAI(sticks)
    elif mode == 3:
        print("You've selected Player vs. Smart AI!")
        game = PersonVSmartAI(sticks)
    else:
        print("You've selected AI vs. AI!")
        game = AIVAI(sticks)


    ##  THIS WILL HAVE TO BE ADDED AFTER THE TURN
    ##  self.turn = self.turns[self.turn]
