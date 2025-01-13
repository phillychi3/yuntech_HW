import requests
import base64
import json

line_notify_token = "Yout Notify Token"

line_notify_api = "https://notify-api.line.me/api/notify"


def lambda_handler(event, context):
    try:
        body = (
            json.loads(event["body"])
            if isinstance(event.get("body"), str)
            else event.get("body", {})
        )
        message = body.get("message")
        image_url = body.get("image_url")
        if message is None:
            return {
                "statusCode": 400,
                "body": 'Missing "message" parameter in the request body',
            }

        headers = {"Authorization": f"Bearer {line_notify_token}"}

        files = {}
        if image_url:
            image_data = base64.b64decode(image_url)
            files = {
                "message": (None, message),
                "imageFile": ("image.jpg", image_data, "image/jpeg"),
            }
            response = requests.post(line_notify_api, headers=headers, files=files)
        else:
            data = {"message": message}
            response = requests.post(line_notify_api, headers=headers, data=data)

        if response.status_code != 200:
            return {
                "statusCode": response.status_code,
                "body": json.dumps(
                    {
                        "error": "Failed to send message",
                        "status": response.status_code,
                        "response_text": response.text,
                        "sent_message": message,
                    }
                ),
            }
        else:
            return {
                "statusCode": 200,
                "body": json.dumps(
                    {
                        "message": "Message sent successfully",
                        "status": response.status_code,
                        "response_text": response.text,
                        "sent_message": message,
                    }
                ),
            }
    except Exception as e:
        return {"statusCode": 500, "body": f"Error: {str(e)}"}
