from bin.thinker.model.question.questiondigits import QuestionDigits
from .questioncreator import QuestionCreator


class CreatorDigitsQuestion(QuestionCreator):
    """
    Override the factory method to return an instance of a
    QuestionDigits.
    """

    def _createQuestion(self, values):
        return QuestionDigits(values['value'], [], values['key'], values['reiterable'])
