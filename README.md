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
