from thinker.model.question.questionbetween import QuestionBetween
from .questioncreator import QuestionCreator


class CreatorBetweenQuestion(QuestionCreator):

    # Override the factory method to return an instance of a
    # QuestionBetween.

    def _createQuestion(self, values):
        return QuestionBetween(values['value'], [], values['key'], values['reiterable'])
