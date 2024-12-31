# Lambda 函數代碼
import json
import boto3
import base64
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # 初始化 AWS Rekognition 客戶端
    rekognition = boto3.client('rekognition')
    
    try:
        # 從 API Gateway 請求中獲取圖片
        image_content = event['body']
        
        # 如果圖片是 base64 編碼的
        if 'isBase64Encoded' in event and event['isBase64Encoded']:
            image_content = base64.b64decode(image_content)
        
        # 調用 Rekognition 進行物件偵測
        response = rekognition.detect_labels(
            Image={
                'Bytes': image_content
            },
            MaxLabels=10,
            MinConfidence=70
        )
        
        # 處理辨識結果
        labels = [{
            'name': label['Name'],
            'confidence': round(label['Confidence'], 2)
        } for label in response['Labels']]
        
        # 返回結果
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'  # 允許跨域請求
            },
            'body': json.dumps({
                'success': True,
                'labels': labels
            })
        }
        
    except ClientError as e:
        # 處理 AWS 服務錯誤
        return {
            'statusCode': 500,
            'body': json.dumps({
                'success': False,
                'error': str(e)
            })
        }
    except Exception as e:
        # 處理其他錯誤
        return {
            'statusCode': 400,
            'body': json.dumps({
                'success': False,
                'error': str(e)
            })
        }