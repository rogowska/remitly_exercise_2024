import json
from json import JSONDecodeError


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

        if len(jsonFile["PolicyName"]) > 128:
            raise Exception('field "PolicyName" has reached length limit of 128')

        if not isinstance(jsonFile["PolicyDocument"], dict):
            raise Exception('field "PolicyDocument" has no JSON type')

        if jsonFile["PolicyDocument"]["Statement"][0]["Resource"] == "*":
            return False
        else:
            return True

    except JSONDecodeError as e:
        raise Exception('file passed to function isJsonCorrect() has no JSON type') from e
