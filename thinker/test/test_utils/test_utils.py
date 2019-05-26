import unittest
import random
import os

from thinker.utils.utils import Utils

class TestUtils(unittest.TestCase):

    def test_PrimesIsNotEmpty(self):
        self.assertIsNot(len(Utils().primes()), 0)
        print("test_PrimesIsNotEmpty --> Passed")

    def test_PrimesIsList(self):
        self.assertIsInstance(Utils().primes(), list)
        print("test_PrimesIsList --> Passed")

    def test_PrimesNoGreaterThanBound(self):
        bound = random.randint(2, 100)
        primes = Utils().primes(bound=bound)
        self.assertIs(len([i for i in primes if i >= bound]), 0)
        print("test_PrimesNoGreaterThanBound --> Passed")

    def test_getQuestionsPathCorrectExtension(self):
        extension = '.json'
        self.assertIs(Utils().getQuestionsPath().endswith(extension), True)
        print("test_getQuestionsPathCorrectExtension --> Passed")

    def test_getQuestionsPathFileExists(self):
        self.assertIs(os.path.exists(Utils().getQuestionsPath()), True)
        print("test_getQuestionsPathFileExists --> Passed")