
# AWS_Projects
Movie Poster Generator using AWS Bedrock and Lambda
Project Overview
This project implements a serverless movie poster generation service using AWS Lambda, Amazon Bedrock (Stable Diffusion XL), and S3. The service takes a text prompt as input and generates a corresponding movie poster image.

Architecture
AWS Lambda: Handles the main processing logic
Amazon Bedrock: Uses Stability AI's Stable Diffusion XL model for image generation
Amazon S3: Stores the generated poster images
Features
Text-to-image generation for movie posters
Automatic image storage in S3
Presigned URL generation for secure image access
Error handling and logging
Unique filename generation with timestamps
Prerequisites
AWS Account with appropriate permissions
Access to AWS Bedrock
S3 bucket named "1movieposterdesign1"
IAM role with necessary permissions for Lambda:
bedrock-runtime:InvokeModel
s3:PutObject
s3:GetObject
Input Format
The Lambda function expects an event with the following structure:

    
{
    "prompt": "your text description for the movie poster"
}

    

    
Output Format
Successful response:

    
{
    "statusCode": 200,
    "body": {
        "posterName": "posterName2024-01-01-12-00-00.jpg"
    }
}

    

    
Error Handling
The function includes error handling for:

Invalid input validation
API call failures
S3 upload issues
Configuration
Key parameters in the code:

Model ID: stability.stable-diffusion-xl-v1
Image generation parameters:
cfg_scale: 10
steps: 30
seed: 0
S3 bucket name: "1movieposterdesign1"
URL expiration time: 3600 seconds (1 hour)
Deployment
Create an S3 bucket
Create a Lambda function with the provided code
Configure appropriate IAM roles
Set up necessary environment variables
Deploy the function
Usage
Invoke the Lambda function with a prompt
The function generates an image using Bedrock
Image is saved to S3
A file name is returned in the response
License
[Your License Here]

Contact
[Your Contact Information]

Acknowledgments
AWS Bedrock
Stability AI's Stable Diffusion XL
