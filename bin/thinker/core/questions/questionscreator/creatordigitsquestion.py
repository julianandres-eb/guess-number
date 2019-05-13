from .questioncreator import QuestionCreator
from bin.thinker.model.question.questiondigits import QuestionDigits

class CreatorDigitsQuestion(QuestionCreator):

    """
    Override the factory method to return an instance of a
    QuestionDigits.
    """

    def _createQuestion(self, values):
        return QuestionDigits(values['value'], [], values['key'], values['reiterable'])