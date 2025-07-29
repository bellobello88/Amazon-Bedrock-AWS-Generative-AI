# AWS Lambda Bedrock Text Generation Function

This Lambda function integrates with Amazon Bedrock to generate text responses using the Cohere Command Light model.

## Overview

This function takes a prompt as input and returns generated text using Amazon Bedrock's AI capabilities. It utilizes the `cohere.command-light-text-v14` model for text generation.

## Requirements

- AWS Lambda
- Python 3.x
- IAM Role with permissions for:
  - Amazon Bedrock
  - CloudWatch Logs
- Required Python packages:
  - boto3
  - json

## Configuration

### Environment Variables

No environment variables are required for this function.

### IAM Permissions

The Lambda function's execution role needs the following permissions:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel"
            ],
            "Resource": "*"
        }
    ]
}

