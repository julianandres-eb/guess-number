import os, itertools
class Utils:

    def __init__(self):
        pass

    def getQuestionsPath():
        return os.getcwd() + "/thinker/model/question/listQuestions.json"


    def primes(self, n):
        primes = [2]

        for i in range(3, n, 2):
            if not any(i % prime == 0 for prime in primes):
                primes.append(i)

        return primes