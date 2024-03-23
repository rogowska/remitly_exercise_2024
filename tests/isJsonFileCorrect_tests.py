import unittest
from isJsonFileCorrect import isJsonFileCorrect


class TestsIsJsonFileCorrect(unittest.TestCase):

    def setUp(self):
        self.isNotJson = open("resources/isNotJson.txt", "r")
        self.noPolicyName = open("resources/noPolicyName.json", "r")
        self.noPolicyDocument = open("resources/noPolicyDocument.json", "r")
        self.noResource = open("resources/noResource.json", "r")
        self.policyNameWrongType = open("resources/policyNameWrongType.json", "r")
        self.policyDocumentWrongType = open("resources/policyDocumentWrongType.json", "r")
        self.resourceWrongType = open("resources/resourceWrongType.json", "r")
        self.policyNameLengthLimit = open("resources/policyNameLengthLimit.json", "r")
        self.singleAsterisk = open("resources/singleAsterisk.json", "r")
        self.multipleAsterisks = open("resources/multipleAsterisks.json", "r")
        self.emptyResourceField = open("resources/emptyResourceField.json", "r")
        self.someTextInResourceField = open("resources/someTextInResourceField.json", "r")
        self.versionValueWrongFormat = open("resources/versionValueWrongFormat.json", "r")

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
        self.assertTrue('field "PolicyName" has length out of range 1-128' in str(context.exception))

    def testPolicyNamePatternValidation(self): pass

    def testWrongPolicyDocumentFieldType(self):
        with self.assertRaises(Exception) as context:
            isJsonFileCorrect(self.policyDocumentWrongType)
        self.assertTrue('field "PolicyDocument" has no JSON type' in str(context.exception))

    def testVersionFieldMissing(self): pass

    def testWrongVersionFieldType(self): pass

    def testWrongVersionFieldFormat(self):
        with self.assertRaises(Exception) as context:
            isJsonFileCorrect(self.versionValueWrongFormat)
        self.assertTrue('value of field "Version" does not match the pattern YYYY-MM-DD' in str(context.exception))

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

    def testMultipleStatements(self): pass

    def testMultipleStatementsOneAsterisk(self): pass

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
        self.versionValueWrongFormat.close()


if __name__ == '__main__':
    unittest.main()
