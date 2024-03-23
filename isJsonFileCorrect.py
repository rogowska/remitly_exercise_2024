import json
from json import JSONDecodeError
import re
import datetime


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
            raise Exception('field "PolicyName" has length out of range 1-128')

        if not re.match(r"[\w+=,.@-]+", jsonFile["PolicyName"]):
            raise Exception('value of field "PolicyName" does not match the pattern [\\w+=,.@-]+')

        if not isinstance(jsonFile["PolicyDocument"], dict):
            raise Exception('field "PolicyDocument" has no JSON type')

        if "Version" not in jsonFile["PolicyDocument"]['Version']:
            raise Exception('file has no field "Version"')

        if not isinstance(jsonFile["PolicyDocument"]['Version'], str):
            raise Exception('field "Version" has no string type')

        datetime.date.fromisoformat(jsonFile["PolicyDocument"]['Version'])

        #if not re.match(r"^\d{4}-\d{2}-\d{2}$", jsonFile["PolicyDocument"]['Version']):
            #raise Exception('value of field "Version" does not match the pattern YYYY-MM-DD')

        statements_number = len(jsonFile["PolicyDocument"]["Statement"])

        for i in range(statements_number):

            if "Sid" in jsonFile["PolicyDocument"]["Statement"][i]:
                if not re.match(r"[a-zA-Z0-9]+", jsonFile["PolicyDocument"]["Statement"][i]["Sid"]):
                    raise Exception('value of field "Sid" does not match the pattern [a-zA-Z0-9]+')

            if jsonFile["PolicyDocument"]["Statement"][i]["Effect"] != "Allow" or \
                    jsonFile["PolicyDocument"]["Statement"][i]["Effect"] != "Deny":
                raise Exception('value of field "Effect" is not equal either "Allow" or "Deny"')
            # action

            if "Resource" not in jsonFile["PolicyDocument"]["Statement"][0]:
                raise Exception('file has no field "Resource"')

            if not isinstance(jsonFile["PolicyDocument"]["Statement"][0]["Resource"], str):
                raise Exception('field "Resource" has no string type')

            if jsonFile["PolicyDocument"]["Statement"][0]["Resource"] == "*":
                return False

        return True

    except JSONDecodeError as e:
        raise Exception('file passed to function isJsonCorrect() has no JSON type') from e
    except ValueError as e:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD") from e
