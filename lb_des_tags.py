import boto3
client = boto3.client('elbv2')

response = client.describe_tags(
    ResourceArns=[
        'arn:aws:elasticloadbalancing:eu-west-1:378457291432:loadbalancer/app/cbsextprod/d091053ef96a5b44',
    ]
)
for resp in response['TagDescriptions']:
    tags=resp['Tags']
    print(f"Tags are {tags}")