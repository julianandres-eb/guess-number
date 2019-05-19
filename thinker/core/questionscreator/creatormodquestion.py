from thinker.model.question import QuestionMod
from .questioncreator import QuestionCreator


class CreatorModQuestion(QuestionCreator):

    # Override the factory method to return an instance of a
    # QuestionPosition.

    def _createQuestion(self, values):
        return QuestionMod(values['value'], [], values['key'], values['reiterable'])
