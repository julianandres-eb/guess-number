import unittest
import random
import os

from thinker.utils.utils import Utils

class TestUtils(unittest.TestCase):

    def test_PrimesIsNotEmpty(self):
        self.assertIsNot(len(Utils().primes()), 0)

    def test_PrimesIsList(self):
        self.assertIsInstance(Utils().primes(), list)

    def test_PrimesNoGreaterThanBound(self):
        bound = random.randint(2, 100)
        primes = Utils().primes(bound=bound)
        self.assertIs(len([i for i in primes if i >= bound]), 0)

    def test_getQuestionsPathCorrectExtension(self):
        extension = '.json'
        self.assertIs(Utils().getQuestionsPath().endswith(extension), True)

    def test_getQuestionsPathFileExists(self):
        self.assertIs(os.path.exists(Utils().getQuestionsPath()), True)