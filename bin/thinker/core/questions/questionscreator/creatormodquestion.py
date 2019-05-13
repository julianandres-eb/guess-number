from .questioncreator import QuestionCreator
from bin.thinker.model.question.questionmod import QuestionMod

class CreatorModQuestion(QuestionCreator):

    """
    Override the factory method to return an instance of a
    QuestionPosition.
    """

    def _createQuestion(self, values):
        return QuestionMod(values['value'], [], values['key'], values['reiterable'])