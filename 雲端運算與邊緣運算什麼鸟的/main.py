import json
import boto3
import os


def lambda_handler(event, context):
    bedrock = boto3.client(
        service_name="bedrock-runtime", region_name=os.environ["AWS_REGION"]
    )

    try:
        body = event.get("body")
        if isinstance(body, str):
            body = json.loads(body)

        request_body = {
            "inputs": body.get("inputs", []),
            "   ": {
                "max_new_tokens": body.get("parameters", {}).get("max_new_tokens", 512),
                "top_p": body.get("parameters", {}).get("top_p", 0.9),
                "temperature": body.get("parameters", {}).get("temperature", 0.6),
            },
        }

        response = bedrock.invoke_model(
            modelId="us.meta.llama3-2-11b-instruct-v1:0",
            contentType="application/json",
            accept="application/json",
            body=json.dumps(request_body),
        )
        response_body = json.loads(response["body"].read())

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(response_body),
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": str(e)}),
        }
