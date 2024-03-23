import json
from json import JSONDecodeError
import re


def isJsonFileCorrect(jsonFile):
    try:
        # trying parsing json from a file
        jsonFile = json.load(jsonFile)

        if "PolicyName" not in jsonFile:
            raise Exception('file has no field "PolicyName"')

        if "PolicyDocument" not in jsonFile:
            raise Exception('file has no field "PolicyDocument"')

        if not isinstance(jsonFile["PolicyName"], str):
            raise Exception('field "PolicyName" has no string type')

        if len(jsonFile["PolicyName"]) > 128 or len(jsonFile["PolicyName"]) < 1:
            raise Exception('field "PolicyName" has lenght out of range 1-128')

        if not re.match(r"[\w+=,.@-]+", jsonFile["PolicyName"]):
            raise Exception('value of field "PolicyName" does not match the pattern [\\w+=,.@-]+')

        if not isinstance(jsonFile["PolicyDocument"], dict):
            raise Exception('field "PolicyDocument" has no JSON type')

        statements_number = len(jsonFile["PolicyDocument"]["Statement"])

        for i in range(statements_number):

            if "Sid" in jsonFile["PolicyDocument"]["Statement"][i]:
                if not re.match(r"[a-zA-Z0-9]+", jsonFile["PolicyDocument"]["Statement"][i]["Sid"]):
                    raise Exception('value of field "Sid" does not match the pattern [a-zA-Z0-9]+')

        # effect

        # action

        # JEŚLI jest condition ??

        if "Resource" not in jsonFile["PolicyDocument"]["Statement"][0]:
            raise Exception('file has no field "Resource"')

        if not isinstance(jsonFile["PolicyDocument"]["Statement"][0]["Resource"], str):
            raise Exception('field "Resource" has no string type')

        if jsonFile["PolicyDocument"]["Statement"][0]["Resource"] == "*":
            return False
        else:
            return True

    except JSONDecodeError as e:
        raise Exception('file passed to function isJsonCorrect() has no JSON type') from e
