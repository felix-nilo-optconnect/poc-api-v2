import json


def handler(event, context):
    """
    Lambda Authorizer to protect the /auth-get endpoint.
    Validates a token in the 'Authorization' header.
    """
    token = event.get("authorizationToken")
    method_arn = event.get("methodArn")

    if token == "allow":
        return generate_policy("user", "Allow", method_arn)
    elif token == "deny":
        return generate_policy("user", "Deny", method_arn)
    else:
        # API Gateway response with 401 Unauthorized.
        raise Exception("Unauthorized")


def generate_policy(principal_id, effect, resource):
    auth_response = {
        "principalId": principal_id,
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {"Action": "execute-api:Invoke", "Effect": effect, "Resource": resource}
            ],
        },
    }
    return auth_response
