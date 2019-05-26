import os


class Utils:

    baseDirectory: str

    def __init__(self):
        self.baseDirectory = os.getcwd()

    def getQuestionsPath(self):
        return self.baseDirectory + "/thinker/model/question/listQuestions.json"


    def primes(self, bound=10):
        primes = [2]

        for i in range(3, bound, 2):
            if not any(i % prime == 0 for prime in primes):
                primes.append(i)

        return primes
