import boto3

client = boto3.client('rds')

response = client.add_tags_to_resource(
    ResourceName='arn:aws:rds:eu-west-1:378457291432:db:afrprdcst01',
    Tags=[
        {
            'Key': 'Name',
            'Value': 'test'
        },
    ]
)