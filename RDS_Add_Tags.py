import boto3

client = boto3.client('rds')

response = client.add_tags_to_resource(
    ResourceName='',
    Tags=[
        {
            'Key': 'Name',
            'Value': 'test'
        },
    ]
)
