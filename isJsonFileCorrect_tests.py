from json import JSONDecodeError
import unittest
from isJsonFileCorrect import isJsonFileCorrect


class TestsIsJsonFileCorrect(unittest.TestCase):

    def setUp(self):
        self.singleAsterisk = open("singleAsterisk.json", "r")
        self.isNotJson = open("isNotJson.txt", "r")

    def testForNotJsonFile(self):
        with self.assertRaises(Exception) as context:
            isJsonFileCorrect(self.isNotJson)
        self.assertTrue('file passed to function isJsonCorrect had no JSON type' in str(context.exception))

    def testForSingleAsteriskCorrectJsonFile(self):
        assert isJsonFileCorrect(self.singleAsterisk) == False


if __name__ == '__main__':
    unittest.main()
