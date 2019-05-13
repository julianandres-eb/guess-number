from bin.thinker.model.question.questionposition import QuestionPosition
from .questioncreator import QuestionCreator


class CreatorPositionQuestion(QuestionCreator):
    """
    Override the factory method to return an instance of a
    QuestionPosition.
    """

    def _createQuestion(self, values):
        return QuestionPosition(values['value'], [], values['key'], values['reiterable'])
