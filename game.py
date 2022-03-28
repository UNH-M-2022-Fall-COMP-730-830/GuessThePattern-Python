# python3

from context import GameContext

class Game:
    """ Yes/No question game. It presents a sequence of questions to a user. The sequence changes
    depending on the user's answers to the previous questions.
    """

    def __init__(self, context: GameContext):
        # Use self.context to interact with the UI. For example, to display a question or exit the game.
        self.context = context

    def start(self):
        """It's called when a user is ready to play the game.
        Handles the game setup, such as showing the initial question.
        """
        self.context.show_question("Welcome to the game! " \
        "Think of a design pattern and answer these following yes/no questions. " \
        "Ready?")

    def answer_yes(self):
        """It's called when a user answers YES to a question.
         Handles the transition to the next question or exits the game.
         """
        self.context.show_question("You answered YES. Continue?")

    def answer_no(self):
        """It's called when a user answers NO to a question.
        Handles the transition to the next question or exits the game.
        """
        self.context.end_game()