# python3

from game import Game
from context import GameContext

class Context(GameContext):
    """Responsible for handling interaction with the game UI."""

    def show_question(self, question):
        """Displays the question to a user."""
        answer = input(question)
        if(answer == "yes"):
            self.game.answer_yes()
        elif(answer == "no"):
            self.game.answer_no()
        else:
            print("Unknown input " + answer)

    def end_game(self):
        """Exits the game."""
        print("Ending game...")
        pass

def main():
    context = Context()
    context.game = Game(context)
    context.game.start()
    context.game = None

if __name__ == "__main__":
    main()
