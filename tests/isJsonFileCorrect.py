import json
from json import JSONDecodeError
import re


def isJsonFileCorrect(jsonFile):
    sids = set()
    flag = True
    try:

        if not jsonFile.readable():
            raise Exception('file is not opened in read mode')

        # trying parsing json from a file
        jsonFile = json.load(jsonFile)

        if "PolicyName" not in jsonFile:
            raise Exception('file has no field "PolicyName"')

        if "PolicyDocument" not in jsonFile:
            raise Exception('file has no field "PolicyDocument"')

        if not isinstance(jsonFile["PolicyName"], str):
            raise Exception('field "PolicyName" has no string type')

        if len(jsonFile["PolicyName"]) > 128 or len(jsonFile["PolicyName"]) < 1:
            raise Exception('field "PolicyName" has length out of range 1-128')

        if not re.match(r"[\w+=,.@-]+", jsonFile["PolicyName"]):
            raise Exception('value of field "PolicyName" does not match the pattern [\\w+=,.@-]+')

        if not isinstance(jsonFile["PolicyDocument"], dict):
            raise Exception('field "PolicyDocument" has no JSON type')

        if "Version" not in jsonFile["PolicyDocument"]:
            raise Exception('file has no field "Version"')

        if not isinstance(jsonFile["PolicyDocument"]['Version'], str):
            raise Exception('field "Version" has no string type')

        if not re.match(r"^\d{4}-\d{2}-\d{2}$", jsonFile["PolicyDocument"]["Version"]):
            raise Exception('value of field "Version" does not match the pattern YYYY-MM-DD')

        if "Statement" not in jsonFile["PolicyDocument"]:
            raise Exception('file has no field "Statement"')

        if not isinstance(jsonFile["PolicyDocument"]['Statement'], list):
            raise Exception('field "Statement" is not a list')

        statements_number = len(jsonFile["PolicyDocument"]["Statement"])

        if statements_number < 1:
            raise Exception('file has no statements')

        for i in range(statements_number):

            if "Sid" in jsonFile["PolicyDocument"]["Statement"][i]:
                if not re.match(r"[a-zA-Z0-9]+", jsonFile["PolicyDocument"]["Statement"][i]["Sid"]):
                    raise Exception('value of field "Sid" does not match the pattern [a-zA-Z0-9]+'
                                    ' in the ' + str(i) + ' statement')
                if jsonFile["PolicyDocument"]["Statement"][i]["Sid"] not in sids:
                    sids.add(jsonFile["PolicyDocument"]["Statement"][i]["Sid"])
                else:
                    raise Exception('file has not unique sids')

            if "Effect" not in jsonFile["PolicyDocument"]["Statement"][i]:
                raise Exception('file has no field "Effect" in the ' + str(i) + ' statement')

            if (jsonFile["PolicyDocument"]["Statement"][i]["Effect"] != "Allow" and
                    jsonFile["PolicyDocument"]["Statement"][i]["Effect"] != "Deny"):
                raise Exception('value of field "Effect" is not equal either "Allow" or "Deny"'
                                ' in the ' + str(i) + ' statement')

            if "Action" not in jsonFile["PolicyDocument"]["Statement"][i]:
                raise Exception('file has no field "Action" in the ' + str(i) + ' statement')

            if "Resource" not in jsonFile["PolicyDocument"]["Statement"][i]:
                raise Exception('file has no field "Resource" in the ' + str(i) + ' statement')

            if not isinstance(jsonFile["PolicyDocument"]["Statement"][i]["Resource"], str):
                raise Exception('field "Resource" has no string type in the ' + str(i) + ' statement')

            if jsonFile["PolicyDocument"]["Statement"][i]["Resource"] == "*":
                flag = False

        return flag

    except JSONDecodeError as e:
        raise Exception('file passed to function isJsonCorrect() has no JSON type') from e
