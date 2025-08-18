Amazon Bedrock Knowledge Base with Lambda Integration

This project demonstrates how to create a question-answering system using Amazon Bedrock Knowledge Base, AWS Lambda, and API Gateway.

Architecture Overview

![Architecture Diagram]

S3 Bucket (Data Source)
Amazon Bedrock Knowledge Base
AWS Lambda Function
API Gateway
Claude Instant v1 Model
Prerequisites

AWS Account with appropriate permissions
AWS CLI configured
Python 3.9+
boto3 library
Implementation Steps

1. Data Source Setup

# Create S3 Bucket
aws s3 mb s3://knowledgebaseaws01

# Upload files to S3
aws s3 cp your-files s3://knowledgebaseaws01/

2. Amazon Bedrock Knowledge Base Configuration

Create Knowledge Base
Configure Data Source (S3)
Set up Chunking parameters
Select Embedding Model
Configure Vector Store
3. AWS Lambda Function Setup

Create IAM Role with necessary permissions:

AWSLambdaBasicExecutionRole
BedrockKnowledgeBaseAccess
S3ReadAccess
Create Lambda Function:

Runtime: Python 3.9
Handler: lambda_function.lambda_handler
Deploy Lambda Layer for boto3:

# Create and upload boto3 layer
zip -r boto3-layer.zip python/
aws lambda publish-layer-version --layer-name boto3-layer --zip-file fileb://boto3-layer.zip

4. API Gateway Integration

Create REST API
Configure Lambda Integration
Deploy API
Configuration

# Lambda Environment Variables
KNOWLEDGE_BASE_ID = '5IS2LUZPOO'
MODEL_ARN = 'arn:aws:bedrock:us-west-2::foundation-model/anthropic.claude-instant-v1'

Usage

Send POST request to API endpoint:

{
    "prompt": "Your question here"
}

Error Handling

Common issues and solutions:

boto3 version mismatch - Update using Lambda Layer
Timeout issues - Increase Lambda timeout
Permission errors - Check IAM roles
Security

Implement API Gateway authentication
Use least privilege IAM roles
Encrypt sensitive data
Maintenance

Regular monitoring of Lambda logs
Update boto3 layers as needed
Monitor Knowledge Base performance
