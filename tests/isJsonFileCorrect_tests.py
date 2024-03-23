import unittest
from isJsonFileCorrect import isJsonFileCorrect


class TestsIsJsonFileCorrect(unittest.TestCase):

    def setUp(self):
        self.isNotJson = open("tests/resources/isNotJson.txt", "r")
        self.noPolicyName = open("tests/resources/noPolicyName.json", "r")
        self.noPolicyDocument = open("tests/resources/noPolicyDocument.json", "r")
        self.noResource = open("tests/resources/noResource.json", "r")
        self.policyNameWrongType = open("tests/resources/policyNameWrongType.json", "r")
        self.policyDocumentWrongType = open("tests/resources/policyDocumentWrongType.json", "r")
        self.resourceWrongType = open("tests/resources/resourceWrongType.json", "r")
        self.policyNameLengthLimit = open("tests/resources/policyNameLengthLimit.json", "r")
        self.singleAsterisk = open("tests/resources/singleAsterisk.json", "r")
        self.multipleAsterisks = open("tests/resources/multipleAsterisks.json", "r")
        self.emptyResourceField = open("tests/resources/emptyResourceField.json", "r")
        self.someTextInResourceField = open("tests/resources/someTextInResourceField.json", "r")

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

    def testPolicyNameLengthValidation(self):
        with self.assertRaises(Exception) as context:
            isJsonFileCorrect(self.policyNameLengthLimit)
        self.assertTrue('field "PolicyName" has lenght out of range 1-128' in str(context.exception))

    def testPolicyNamePatternValidation(self): pass

    def testWrongPolicyDocumentFieldType(self):
        with self.assertRaises(Exception) as context:
            isJsonFileCorrect(self.policyDocumentWrongType)
        self.assertTrue('field "PolicyDocument" has no JSON type' in str(context.exception))

    def testVersionFieldMissing(self): pass

    def testWrongVersionFieldType(self): pass

    def testWrongVersionFieldFormat(self): pass

    def testStatementFieldMissing(self): pass

    def testWrongStatementFieldType(self): pass

    def testSidPatternValidation(self): pass

    def testEffectValueValidation(self): pass

    def testActionValueValidation(self): pass

    def testResourceFieldMissing(self):
        with self.assertRaises(Exception) as context:
            isJsonFileCorrect(self.noResource)
        self.assertTrue('file has no field "Resource"' in str(context.exception))

    def testWrongResourceFieldType(self):
        with self.assertRaises(Exception) as context:
            isJsonFileCorrect(self.resourceWrongType)
        self.assertTrue('field "Resource" has no string type' in str(context.exception))

    def testSingleAsteriskInResourceField(self):
        self.assertFalse(isJsonFileCorrect(self.singleAsterisk))

    def testEmptyResouceField(self):
        self.assertTrue(isJsonFileCorrect(self.emptyResourceField))

    def testMultipleAsterisksInResourceField(self):
        self.assertTrue(isJsonFileCorrect(self.multipleAsterisks))

    def testSomeTextInResourceField(self):
        self.assertTrue(isJsonFileCorrect(self.someTextInResourceField))

    def tearDown(self):
        self.isNotJson.close()
        self.noPolicyName.close()
        self.noPolicyDocument.close()
        self.noResource.close()
        self.policyNameWrongType .close()
        self.policyDocumentWrongType.close()
        self.resourceWrongType.close()
        self.policyNameLengthLimit.close()
        self.singleAsterisk.close()
        self.multipleAsterisks.close()
        self.emptyResourceField.close()
        self.someTextInResourceField.close()


if __name__ == '__main__':
    unittest.main()
