import json
import boto3
client = boto3.client('bedrock-runtime')

def lambda_handler(event, context):
    #Store the input in a variable,
    input_prompt= event['prompt']
    print(input_prompt)
    # Create Request Syntax - get details from console & body should be json obkect - use json.dumps for body
    client_bedrockrequest =client.invoke_model(
        contentType='application/json',
        accept='application/json',
        modelId='cohere.command-light-text-v14'
        body=json.dumps({
            "prompt": input_prompt,
            "temperature": 0.9,
            "p":0.75,
            "maxTokens": 1000}))
    #print(client_bedrockrequest)


    #Convert Streaming Body to Bytes(.read method) and then Byte to String using json.loads#
    client_bedrock_byte =client_bedrockrequest['body'].read()
    #Print the event and type, Stroe the input in a variable,
    #print(client_bedrock)
    #print(type(client_bedrock_byte))
    client_bedrock = json.loads(client_bedrock_byte)
    #print(client_bedrock)
    #indate the return from changing the 'body'
    client_final_response = client_bedrock_string['generations'][0]['text']
    print(client_final_response)

    return {
        'statusCode': 200,
        'body': json.dumps(Hello from Bedrock! + client_final_response)


    }
