import boto3

client = boto3.client('rds')

response = client.remove_tags_from_resource(
    ResourceName='',
    TagKeys=[
        'Name',
    ]
)
