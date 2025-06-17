import json


def handler(event, context):
    """
    Lambda Authorizer to secured endpoint /auth-get.
    Only invoked if the Lambda Authorizer allows it.
    """
    response = {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "Access granted to the /auth-get endpoint with authorization token!"
            }
        ),
    }
    return response
