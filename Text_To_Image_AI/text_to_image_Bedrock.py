import json
import boto3
import base64
import datetime
client_bedrock =boto3.client('bedrock-runtime')
client_s3 =boto3.client('s3')

def lambda_handler(event, context):
    # TODO implement
    # Check input
    try:
        print(f"Received event:{event}")
        if not event or 'prompt'not in event:
            print("Invalid input" )
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid input')
            }
        # Get and print input
        input_prompt = event['prompt']
        print(f"Received prompt: {input_prompt}")

        # call Bedrock API
        response_bedrock = client_bedrock.invoke_model(
            contentType = 'application/json', 
            accept = 'application/JSON',
            modelId ='stability.stable-diffusion-xl-v1',
            body =json.dumps({"text_prompts":[{"text":input_prompt}],
            "cfg_scale":10,
            "steps":30,
            "seed":0
            })
        )
        # process response
        response_bedrock_byte = json.loads(response_bedrock['body'].read())
        print(response_bedrock_byte)
        response_bedrock_base64 = response_bedrock_byte['artifacts'][0]['base64']
        response_bedrock_finalimage = base64.b64decode(response_bedrock_base64)
        print(response_bedrock_finalimage)

        # generating file name
        poster_name = f'posterName{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.jpg'

        # upload to s3
        response_s3= client_s3.put_object(
            Bucket ='1movieposterdesign1',
            Body= response_bedrock_finalimage,
            Key=poster_name,
            ContentType ='image/jpeg')
        #generate presigned URL
        generate_presigned_url =client_s3.generate_presigned_url('get_object', Params={'Bucket':'1movieposterdesign1','key':poster_name}, ExpiresIn=3600,HttpMethod=None)
        print(generate_presigned_url)

        return {
            'statusCode': 200,
            'body': json.dumps({
            'posterName': poster_name
            })
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps('Internal Server Error')
        }
