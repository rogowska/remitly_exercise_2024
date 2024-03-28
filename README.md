
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

File isJsonFileCorrect_tests_py contains all the unit tests written with the help of unittest python library.

### Covered tests cases are:

1. Checking if the file parameter is JSON.
2. Checking if the JSON file has PolicyName field.
3. Checking if the JSON file has PolicyDocument field.
4. Checking if PolicyName has a certain type.
5. Checking if PolicyDocument has a certain type.
6. Checking if PolicyName field has valid length.
7. Checking if PolicyName has valid pattern.


#### Within PolicyDocument scope:

8. Checking if file has Version field.
9. Checking if file has Statement field.
10. Checking if Version field has certain type.
11. Checking if Version field has certain format.
12. Checking if Statement field has certain type.

#### Within Statement scope:

13. Checking if there is at least one statement.
14. Checking if Sid pattern is correct. 
15. Checking if there is Effect field.
16. Checking if Effect field has value equal to either "Allow" or "Deny".
17. Checking if there are Action field.
18. Checking if there is Resource field.
19. Checking if Resource field has certain type.
20. Checking if in the case of multiple statements, they all have unique Sids.

Remaining tests check wether function returns correctly "True" or "False".
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
Ran 25 tests in 0.007s

OK
```
