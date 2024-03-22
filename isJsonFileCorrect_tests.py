import unittest
from isJsonFileCorrect import isJsonFileCorrect


class TestsIsJsonFileCorrect(unittest.TestCase):

    def setUp(self):
        self.singleAsterisk = open("singleAsterisk.json", "r")
        self.isNotJson = open("isNotJson.txt", "r")
        self.noPolicyName = open("noPolicyName.json", "r")
        self.noPolicyDocument = open("noPolicyDocument.json", "r")
        self.policyNameWrongType = open("policyNameWrongType.json", "r")
        self.policyDocumentWrongType = open("policyDocumentWrongType.json", "r")
        self.policyNameLengthLimit = open("policyNameLengthLimit.json", "r")

    def testNotJsonTypeFile(self):
        with self.assertRaises(Exception) as context:
            isJsonFileCorrect(self.isNotJson)
        self.assertTrue('file passed to function isJsonCorrect() has no JSON type' in str(context.exception))

    def testPolicyNameFieldMissing(self):
        with self.assertRaises(Exception) as context:
            isJsonFileCorrect(self.noPolicyName)
        self.assertTrue('file has no field "PolicyName"' in str(context.exception))

    def testPolicyDocumentFieldMissing(self):
        with self.assertRaises(Exception) as context:
            isJsonFileCorrect(self.noPolicyDocument)
        self.assertTrue('file has no field "PolicyDocument"' in str(context.exception))

    def testWrongPolicyNameFieldType(self):
        with self.assertRaises(Exception) as context:
            isJsonFileCorrect(self.policyNameWrongType)
        self.assertTrue('field "PolicyName" has no string type' in str(context.exception))

    def testWrongLenghtOfPolicyName(self):
        with self.assertRaises(Exception) as context:
            isJsonFileCorrect(self.policyNameLengthLimit)
        self.assertTrue('field "PolicyName" has reached length limit of 128' in str(context.exception))

    def testWrongPolicyDocumentFieldType(self):
        with self.assertRaises(Exception) as context:
            isJsonFileCorrect(self.policyDocumentWrongType)
        self.assertTrue('field "PolicyDocument" has no JSON type' in str(context.exception))

    def testSingleAsteriskInResourceField(self):
        self.assertFalse(isJsonFileCorrect(self.singleAsterisk))

    def testEmptyResouceField(self):
        self.assertTrue(isJsonFileCorrect(self.singleAsterisk)) # ???? jak traktowac puste pole

    def testMultipleAsterisksInResourceField(self):
        self.assertTrue(isJsonFileCorrect(self.singleAsterisk)) # nie skonczone, brak dokumentow

    def testCorrectJsonFileWithProperlyFilledFields(self):
        self.assertTrue(isJsonFileCorrect(self.singleAsterisk)) # nie skonczone, brak dokumentow

    def tearDown(self):
        self.singleAsterisk.close()
        self.isNotJson.close()
        self.noPolicyName.close()
        self.noPolicyDocument.close()
        self.policyNameWrongType .close()
        self.policyDocumentWrongType.close()
        self.policyNameLengthLimit.close()


if __name__ == '__main__':
    unittest.main()
