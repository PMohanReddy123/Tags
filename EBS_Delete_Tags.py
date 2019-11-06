import boto3
client = boto3.client('ec2')
response1 = client.delete_tags(
    Resources=[
        'vol-Id',
    ],
    Tags=[
        {
            'Key': 'Name1',
            'Value': 'Mohan',
        },
    ],
)
