import boto3
import json

dynamo = boto3.client('dynamodb')


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    operation = event['method']
    
    if operation == 'GET':
        payload = event['queryParameters']
        return respond(None, dynamo.scan(**payload))
    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))

