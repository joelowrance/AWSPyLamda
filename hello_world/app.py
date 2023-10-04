import json
import boto3

# import requests
#https://inwpxxtal7.execute-api.us-east-1.amazonaws.com/Stage/hello
#https://inwpxxtal7.execute-api.us-east-1.amazonaws.com/Prod/hello


def lambda_handler(event, context):
    

    # stage variable doesnt come over when using the test button in the gateway.
    stage_variable_value = (event['stageVariables'] or {'alias': 'unknown'})["alias"]
    #stage_variable_value = event['stageVariables']["alias"]
        #event.get['StageVariables', {}].get('alias', 'wtf')

    # to get access to the s3 bucket, I had to
    # 1. edit the IAM role assigned to the lamda
    # 2  Gave it full permissions, which I didnt want but dont know how to avoid.

    s3 = boto3.client('s3')
    bucket = 'configsjl'
    response = s3.get_object(Bucket=bucket, Key='simplefile.txt')
    content = response['Body'].read().decode('utf-8')
    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {},
        # body needs to be converted to json, not just text that looks like json
        "body": json.dumps({
            "message": {
                "content": content,
                #"event": event,
                "v1": stage_variable_value
            }
        })
    }
