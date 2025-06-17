import json


def handler(event, context):
    """
    Lambda function handler for / and public-get endpoints.
    This function returns a simple message.
    """

    response = {
        "statusCode": 200,
        "body": json.dumps({"message": "Hello from Lambda!"}),
    }
    return response
