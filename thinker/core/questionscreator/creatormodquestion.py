from thinker.model.question.questionmod import QuestionMod
from .questioncreator import QuestionCreator


class CreatorModQuestion(QuestionCreator):

    # Override the factory method to return an instance of a
    # QuestionMod.

    def _createQuestion(self, values):
        return QuestionMod(values['value'], [], values['key'], values['reiterable'])
