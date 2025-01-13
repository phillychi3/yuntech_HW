import json
import boto3
import urllib3
import logging
import time
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def log_event(event_type, details, error=None):
    log_data = {
        "timestamp": datetime.now().isoformat(),
        "event_type": event_type,
        "details": details,
    }
    if error:
        log_data["error"] = str(error)
    logger.info(json.dumps(log_data))


def lambda_handler(event, context):
    start_time = time.time()

    log_event(
        "REQUEST_RECEIVED", {"request_id": context.aws_request_id, "event": event}
    )
    try:
        bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")
    except Exception as e:
        log_event("BEDROCK_CLIENT_INITIALIZATION_FAILED", {}, error=str(e))
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
            },
            "body": json.dumps({"error": "Failed to initialize Bedrock client"}),
        }

    try:
        if "body" in event:
            if isinstance(event["body"], str):
                body = json.loads(event["body"])
            else:
                body = event["body"]
        else:
            body = event

        prompt = body.get("prompt", "")
        image_data = body.get("image", "")

        log_event("REQUEST_PARSED", {"prompt": prompt, "has_image": bool(image_data)})

        messages_content = []

        log_event("REQUEST_PARSED", {"prompt": body.get("prompt", "")})
        if image_data:
            messages_content.append(
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/jpeg",
                        "data": image_data,
                    },
                }
            )

        messages_content.append({"type": "text", "text": prompt})
        request_body = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1000,
            "messages": [{"role": "user", "content": messages_content}],
        }

        response = bedrock.invoke_model(
            modelId="anthropic.claude-3-5-sonnet-20240620-v1:0",
            contentType="application/json",
            accept="application/json",
            body=json.dumps(request_body),
        )

        response_body = json.loads(response["body"].read())
        log_event(
            "BEDROCK_RESPONSE_RECEIVED",
            {"response_length": len(response_body["content"][0]["text"])},
        )
        data = {"message": response_body["content"][0]["text"], "image_url": image_data}

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
            },
            "body": json.dumps(data),
        }

    except Exception as e:
        execution_time = time.time() - start_time
        log_event(
            "ERROR_OCCURRED",
            {
                "execution_time_seconds": execution_time,
                "error_type": type(e).__name__,
                "error_message": str(e),
            },
            error=str(e),
        )
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
            },
            "body": json.dumps({"error": str(e)}),
        }
