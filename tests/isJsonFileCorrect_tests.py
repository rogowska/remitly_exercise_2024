import unittest
from isJsonFileCorrect import isJsonFileCorrect


class TestsIsJsonFileCorrect(unittest.TestCase):

    def setUp(self):
        self.isNotJson = open("resources/isNotJson.txt", "r")

        self.noPolicyName = open("resources/noPolicyName.json", "r")
        self.noPolicyDocument = open("resources/noPolicyDocument.json", "r")
        self.noResource = open("resources/noResource.json", "r")
        self.noVersion = open("resources/noVersion.json", "r")
        self.noStatement = open("resources/noStatement.json", "r")
        self.noStatements = open("resources/noStatements.json", "r")
        self.noEffect = open("resources/noEffect.json", "r")

        self.policyNameWrongType = open("resources/policyNameWrongType.json", "r")
        self.policyDocumentWrongType = open("resources/policyDocumentWrongType.json", "r")
        self.versionWrongType = open("resources/versionWrongType.json", "r")
        self.resourceWrongType = open("resources/resourceWrongType.json", "r")
        self.statementWrongType = open("resources/statementWrongType.json", "r")

        self.sidWrongPattern = open("resources/sidWrongPattern.json", "r")
        self.policyNameLengthLimit = open("resources/policyNameLengthLimit.json", "r")
        self.singleAsterisk = open("resources/singleAsterisk.json", "r")
        self.multipleAsterisks = open("resources/multipleAsterisks.json", "r")
        self.emptyResourceField = open("resources/emptyResourceField.json", "r")
        self.someTextInResourceField = open("resources/someTextInResourceField.json", "r")
        self.versionValueWrongFormat = open("resources/versionValueWrongFormat.json", "r")
        self.effectWrongValue = open("resources/effectWrongValue.json", "r")

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

    def testVersionFieldMissing(self):
        with self.assertRaises(Exception) as context:
            isJsonFileCorrect(self.noVersion)
        self.assertTrue('file has no field "Version"' in str(context.exception))

    def testWrongVersionFieldType(self):
        with self.assertRaises(Exception) as context:
            isJsonFileCorrect(self.versionWrongType)
        self.assertTrue('field "Version" has no string type' in str(context.exception))

    def testWrongVersionFieldFormat(self):
        with self.assertRaises(Exception) as context:
            isJsonFileCorrect(self.versionValueWrongFormat)
        self.assertTrue('value of field "Version" does not match the pattern YYYY-MM-DD' in str(context.exception))

    def testStatementFieldMissing(self):
        with self.assertRaises(Exception) as context:
            isJsonFileCorrect(self.noStatement)
        self.assertTrue('file has no field "Statement"' in str(context.exception))

    def testWrongStatementFieldType(self):
        with self.assertRaises(Exception) as context:
            isJsonFileCorrect(self.statementWrongType)
        self.assertTrue('field "Statement" is not a list' in str(context.exception))

    def testNumberOfStatementsValidation(self):
        with self.assertRaises(Exception) as context:
            isJsonFileCorrect(self.noStatements)
        self.assertTrue('file has no statements' in str(context.exception))

    def testSidPatternValidation(self):
        with self.assertRaises(Exception) as context:
            isJsonFileCorrect(self.sidWrongPattern)
        self.assertTrue('value of field "Sid" does not match the pattern '
                        '[a-zA-Z0-9]+ in the 0 statement' in str(context.exception))

    def testEffectFieldMissing(self):
        with self.assertRaises(Exception) as context:
            isJsonFileCorrect(self.noEffect)
        self.assertTrue('file has no field "Effect" in the 0 statement' in str(context.exception))

    def testEffectValueValidation(self):
        with self.assertRaises(Exception) as context:
            isJsonFileCorrect(self.effectWrongValue)
        self.assertTrue('value of field "Effect" is not equal either "Allow" or "Deny"'
                                ' in the 0 statement' in str(context.exception))

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
        self.noVersion.close()
        self.noStatement.close()
        self.noStatements.close()
        self.noEffect.close()

        self.policyNameWrongType .close()
        self.policyDocumentWrongType.close()
        self.versionWrongType.close()
        self.resourceWrongType.close()
        self.statementWrongType.close()

        self.sidWrongPattern.close()
        self.policyNameLengthLimit.close()
        self.singleAsterisk.close()
        self.multipleAsterisks.close()
        self.emptyResourceField.close()
        self.someTextInResourceField.close()
        self.versionValueWrongFormat.close()
        self.effectWrongValue.close()


if __name__ == '__main__':
    unittest.main()
