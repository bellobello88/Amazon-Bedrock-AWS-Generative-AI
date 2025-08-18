import json
import boto3

#create client connection for bedrock
client_bedrock_knowledge_base = boto3.client('bedrock-agent-runtime')

def lambda_handler(event, context):
    #store the user prompt
    print(event['prompt'])
    user_prompt = event['prompt']
    #use retrieve and generate API
    client_knowledgebase =client_bedrock_knowledge_base.retrieve_and_generate(
        #sessionID='string'>this line is only for chatbot
    input={
        'text': user_prompt
    },
    retrieveAndGenerateConfiguration={
        'type':'KNOWLEDGE_BASE',
        'knowledgeBaseConfiguration': {
            'knowledgeBaseId':'5IS2LUZPOO',
            'modelArn': 'arn:aws:bedrock:us-west-2::foundation-model/anthropic.claude-instant-v1'
                }
            }
        )
    #print(client_knowledgebase['citations'][0]['generatedResponsePart']['textResponsePart'])
    response_kbase_final=client_knowledgebase['output']['text']
    return {
        'statusCode': 200,
        'body': response_kbase_final
    }
