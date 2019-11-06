import boto3

client = boto3.client('rds')

response = client.remove_tags_from_resource(
    ResourceName='arn:aws:rds:eu-west-1:378457291432:db:afrprdcst01',
    TagKeys=[
        'Name',
    ]
)