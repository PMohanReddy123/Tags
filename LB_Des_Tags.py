import boto3
client = boto3.client('elbv2')

response = client.describe_tags(
    ResourceArns=[
        'LB_ARN',
    ]
)
for resp in response['TagDescriptions']:
    tags=resp['Tags']
    print(f"Tags are {tags}")
