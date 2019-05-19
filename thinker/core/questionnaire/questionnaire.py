from .questionsgenerator import QuestionsGenerator


###########################################################
#
# Questionnaire
#
# This class is responsible for having all the questions and
# decide which question the user has to respond
#
###########################################################

class Questionnaire:

    # Declaration of class variables
    questions = []
    answers = {}
    oldResponses = []

    # Init class
    def __init__(self):
        self.initQuestionaire()

    # Get the necessary questions to be answered
    def initQuestionaire(self):

        if not bool(self.questions):
            self.questions = QuestionsGenerator().getAllQuestions()

    ###########################################################
    #
    # askForResponses(oldResponses)
    #
    # oldResponses: list of int that has all possible numbers that
    # the program has performed but they didn't work out
    #
    # Main asking functions
    #
    ###########################################################

    def askForResponses(self, oldResponses):

        self.oldResponses : list = oldResponses

        # We decide which question has to be answered and ask the user for it
        if self.canContinue():
            for question in self.questions:

                # We don't ask the non reiterable questions
                if question.getReiterable() is "n":

                    if len(question.getAnswers()) is 0:
                        self.answers[question.key] = self.ask(question)
                else:
                    self.answers[question.key] = self.ask(question)

        return self.answers

    ###########################################################
    #
    # ask(question)
    #
    # question: current question to respond
    #
    # Generic function to ask for all type of questions
    #
    ###########################################################


    def ask(self, question):

        # Declaration of variables
        solver = self.getSolver(question)
        correct: bool = False
        answer: list = []

        # Until correct
        while correct is False:

            # We ask for a value
            value = solver.askUserValue(self.oldResponses)

            # We create the complete answer to be used within the program
            answer = solver.composeAnswer(value)

            # We check if all is correct
            if solver.validateAnswer(answer):

                # If yes, we save the answer
                answer = solver.saveAnswer(answer)

                # and finalize the iteration
                correct = True

        return answer

    ###########################################################
    #
    # getSolver(question)
    #
    # question: current question to respond
    #
    # Function that returns the solver to question as parameter
    #
    ###########################################################

    def getSolver(self, question):

        try:
            # We create the class who manages the solver
            solver = globals()[self.composeNameClass(question.key)](question)

        # If there's not that solver, we keep going
        except ModuleNotFoundError:
            pass

        # Otherwise we return it
        else:
            return solver

    ###########################################################
    #
    # canContinue
    #
    # Function that mainly checks if number of digits and positions
    # in the system are correct
    #
    ###########################################################

    def canContinue(self):
        digits = 0
        positions = []
        for question in self.questions:
            if len(question.getAnswers()) > 0:
                if question.getKey() is "digits":
                    digits = question.getAnswers()[0]

                if question.getKey() is "position":
                    positions = question.getAnswers()

            if len(positions) is 0 and digits is 0:
                return True
            else:
                if len(positions) is not digits:
                    return True
                else:
                    return False

    def composeNameClass(self, key):
        return "QuestionSolver" + key.capitalize()