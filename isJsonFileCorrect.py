import json
from json import JSONDecodeError


def isJsonFileCorrect(jsonFile):
    try:
        #trying parsing json from a file
        jsonFile = json.load(jsonFile)

        if "PolicyName" not in jsonFile:
            raise Exception('file has no field "PolicyName"')

        if "PolicyDocument" not in jsonFile:
            raise Exception('file has no field "PolicyDocument"')

        if not isinstance(jsonFile["PolicyName"], str):
            raise Exception('field "PolicyName" has no string type"')

        if not isinstance(jsonFile["PolicyDocument"], dict):
            raise Exception('field "PolicyDocument" has no JSON type"')

    except JSONDecodeError as e:
        raise Exception('file passed to function isJsonCorrect() has no JSON type') from e

    # was json file passed as argument OK
    # does it has 2 fields OK
    # do these fields have certain types OK
    # is resource present
    # verification - does it contain single asterisk or smth else FALSE TRUE
    return False
