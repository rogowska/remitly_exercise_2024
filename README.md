
# Remitly Home Exercise 2024

Write a method verifying the input JSON data. Input data format is defined as AWS::IAM::Role Policy ([AWS IAM Role JSON definition and example](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-role-policy.html)). Input JSON might be read from a file. Method shall return logical false if an input JSON Resource field contains a single asterisk and true in any other case.

JSON:

```
{
    "PolicyName": "root",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "IamListAccess",
                "Effect": "Allow",
                "Action": [
                    "iam:ListRoles",
                    "iam:ListUsers"
                ],
                "Resource": "*"
            }
        ]
    }
}
```


## General Info

Solution contains two files:

* isJsonFileCorrect.py
* isJsonFileCorrect_tests_py

isJsonFileCorrect.py contains a method checking wether the file passed to this method is a valid JSON file.
It takes one parameter, file object which we can read from.

File isJsonFileCorrect_tests_py contains all the unit tests written with the help of unittest python library.

### Covered tests cases are:

1. Checking if file is in the read mode.
2. Checking if the file parameter is JSON.
3. Checking if the JSON file has PolicyName field.
4. Checking if the JSON file has PolicyDocument field.
5. Checking if PolicyName has a certain type.
6. Checking if PolicyDocument has a certain type.
7. Checking if PolicyName field has valid length.
8. Checking if PolicyName has valid pattern.


#### Within PolicyDocument scope:

9. Checking if file has Version field.
10. Checking if file has Statement field.
11. Checking if Version field has certain type.
12. Checking if Version field has certain format.
13. Checking if Statement field has certain type.

#### Within Statement scope:

14. Checking if there is at least one statement.
15. Checking if Sid pattern is correct. 
16. Checking if there is Effect field.
17. Checking if Effect field has value equal to either "Allow" or "Deny".
18. Checking if there are Action field.
19. Checking if there is Resource field.
20. Checking if Resource field has certain type.
21. Checking if in the case of multiple statements, they all have unique Sids.

Remaining tests check wether function returns correctly "True" or "False" in the case of the correctly formatted file.
Resources directory contains all the files required to run test cases. Files can be changed in the setUpClass in the test file.

## Technologies

* Python 3.10.11

Used libraries:

* json 
* re
* unittest
## Launch

To run tests, in the command line, in the tests directory run:

```
python isJsonFileCorrect_tests.py
```

The output should show similar:

```
Ran 26 tests in 0.007s

OK
```

You can also open the project in IDE like "PyCharm" or "Visual Studio Code" and run tests directly from there.

## References
[](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-role-policy.html)
[](https://docs.aws.amazon.com/IAM/latest/APIReference/API_PolicyDetail.html)
[](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json)
[](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html)

