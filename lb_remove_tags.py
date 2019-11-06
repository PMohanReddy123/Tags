import boto3
client = boto3.client('elbv2')

response = client.remove_tags(
    ResourceArns=[
        'string',
    ],
    TagKeys=[
        'string',
    ]
)
