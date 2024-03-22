from json import JSONDecodeError
import unittest
from isJsonFileCorrect import isJsonFileCorrect


class TestsIsJsonFileCorrect(unittest.TestCase):

    def setUp(self):
        self.singleAsterisk = open("singleAsterisk.json", "r")
        self.isNotJson = open("isNotJson.txt", "r")
        self.noPolicyName = open("noPolicyName.json", "r")
        self.noPolicyDocument = open("noPolicyDocument.json", "r")

    def NotJsonTypeFile(self):
        with self.assertRaises(Exception) as context:
            isJsonFileCorrect(self.isNotJson)
        self.assertTrue('file passed to function isJsonCorrect had no JSON type' in str(context.exception))

    def PolicyNameFieldMissing(self):
        with self.assertRaises(Exception) as context:
            isJsonFileCorrect(self.noPolicyName)
        self.assertTrue('file has no field "PolicyName"' in str(context.exception))

    def PolicyDocumentFieldMissing(self): pass

    def WrongPolicyNameFieldType(self): pass

    def WrongPolicyDocumentFieldType(self): pass

    def EmptyResouceField(self): pass

    def SingleAsteriskInResourceField(self):
        assert isJsonFileCorrect(self.singleAsterisk) == False

    def MultipleAsterisksInResourceField(self): pass

    def CorrectJsonFileWithProperlyFilledFields(self): pass


if __name__ == '__main__':
    unittest.main()
