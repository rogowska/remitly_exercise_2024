import unittest
from isJsonFileCorrect import isJsonFileCorrect


class TestsIsJsonFileCorrect(unittest.TestCase):

    # opening all files on the beggining of tests and closing them on the end of them

    @classmethod
    def setUpClass(cls):
        cls.isNotJson = open("resources/isNotJson.txt", "r")
        cls.noPolicyName = open("resources/noPolicyName.json", "r")
        cls.noPolicyDocument = open("resources/noPolicyDocument.json", "r")
        cls.noResource = open("resources/noResource.json", "r")
        cls.noVersion = open("resources/noVersion.json", "r")
        cls.noStatement = open("resources/noStatement.json", "r")
        cls.noStatements = open("resources/noStatements.json", "r")
        cls.noEffect = open("resources/noEffect.json", "r")
        cls.noAction = open("resources/noAction.json", "r")

        cls.policyNameWrongType = open("resources/policyNameWrongType.json", "r")
        cls.policyDocumentWrongType = open("resources/policyDocumentWrongType.json", "r")
        cls.policyNameWrongPattern = open("resources/policyNameWrongPattern.json", "r")

        cls.versionWrongType = open("resources/versionWrongType.json", "r")
        cls.resourceWrongType = open("resources/resourceWrongType.json", "r")
        cls.statementWrongType = open("resources/statementWrongType.json", "r")

        cls.sidWrongPattern = open("resources/sidWrongPattern.json", "r")
        cls.policyNameLengthLimit = open("resources/policyNameLengthLimit.json", "r")
        cls.singleAsterisk = open("resources/singleAsterisk.json", "r")
        cls.multipleAsterisks = open("resources/multipleAsterisks.json", "r")
        cls.multipleStatements = open("resources/multipleStatements.json", "r")
        cls.multipleStatementsOneAsterisk = open("resources/multipleStatementsOneAsterisk.json", "r")
        cls.multipleStatementsManyAsterisks = open("resources/multipleStatementsManyAsterisks.json", "r")
        cls.emptyResourceField = open("resources/emptyResourceField.json", "r")
        cls.someTextInResourceField = open("resources/someTextInResourceField.json", "r")
        cls.versionValueWrongFormat = open("resources/versionValueWrongFormat.json", "r")
        cls.effectWrongValue = open("resources/effectWrongValue.json", "r")
        cls.noUniqueSids = open("resources/noUniqueSids.json", "r")

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

    def testPolicyNamePatternValidation(self):
        with self.assertRaises(Exception) as context:
            isJsonFileCorrect(self.policyNameWrongPattern)
        self.assertTrue('value of field "PolicyName" does not match the pattern [\\w+=,.@-]+' in str(context.exception))

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

    def testActionFieldMissing(self):
        with self.assertRaises(Exception) as context:
            isJsonFileCorrect(self.noAction)
        self.assertTrue('file has no field "Action" in the 0 statement' in str(context.exception))

    def testResourceFieldMissing(self):
        with self.assertRaises(Exception) as context:
            isJsonFileCorrect(self.noResource)
        self.assertTrue('file has no field "Resource" in the 0 statement' in str(context.exception))

    def testWrongResourceFieldType(self):
        with self.assertRaises(Exception) as context:
            isJsonFileCorrect(self.resourceWrongType)
        self.assertTrue('field "Resource" has no string type in the 0 statement' in str(context.exception))

    def testSingleAsteriskInResourceField(self):
        self.assertFalse(isJsonFileCorrect(self.singleAsterisk))

    def testEmptyResouceField(self):
        self.assertTrue(isJsonFileCorrect(self.emptyResourceField))

    def testMultipleAsterisksInResourceField(self):
        self.assertTrue(isJsonFileCorrect(self.multipleAsterisks))

    def testSomeTextInResourceField(self):
        self.assertTrue(isJsonFileCorrect(self.someTextInResourceField))

    def testMultipleStatements(self):
        self.assertTrue(isJsonFileCorrect(self.multipleStatements))
        self.assertFalse(isJsonFileCorrect(self.multipleStatementsOneAsterisk))
        self.assertFalse(isJsonFileCorrect(self.multipleStatementsManyAsterisks))

    def testNoUniqueSidsAmongStatements(self):
            with self.assertRaises(Exception) as context:
                isJsonFileCorrect(self.noUniqueSids)
            self.assertTrue('file has not unique sids' in str(context.exception))

    @classmethod
    def tearDownClass(cls):
        cls.isNotJson.close()

        cls.noPolicyName.close()
        cls.noPolicyDocument.close()
        cls.noResource.close()
        cls.noVersion.close()
        cls.noStatement.close()
        cls.noStatements.close()
        cls.noEffect.close()
        cls.noAction.close()

        cls.policyNameWrongType.close()
        cls.policyDocumentWrongType.close()
        cls.versionWrongType.close()
        cls.resourceWrongType.close()
        cls.statementWrongType.close()

        cls.sidWrongPattern.close()
        cls.policyNameLengthLimit.close()
        cls.singleAsterisk.close()
        cls.multipleAsterisks.close()
        cls.multipleStatements.close()
        cls.multipleStatementsOneAsterisk.close()
        cls.multipleStatementsManyAsterisks.close()
        cls.emptyResourceField.close()
        cls.someTextInResourceField.close()
        cls.versionValueWrongFormat.close()
        cls.effectWrongValue.close()
        cls.noUniqueSids.close()
        cls.policyNameWrongPattern.close()


if __name__ == '__main__':
    unittest.main()
