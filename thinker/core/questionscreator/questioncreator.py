import abc


class QuestionCreator(metaclass=abc.ABCMeta):

    # Declare the factory method, which returns an object of type Question.
    # Creator may also define a default implementation of the factory
    # method that returns a default ConcreteQuestion object.
    # Call the factory method to create a Question object.

    def __init__(self):
        pass

    @abc.abstractmethod
    def _createQuestion(self, values):
        pass
