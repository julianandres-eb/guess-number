from bin.thinker.model.question.questiongoodregular import QuestionGoodregular
from .questioncreator import QuestionCreator


class CreatorGoodregularQuestion(QuestionCreator):
    """
    Override the factory method to return an instance of a
    QuestionGoodRegular.
    """

    def _createQuestion(self, values):
        return QuestionGoodregular(values['value'], [], values['key'], values['reiterable'])
