import boto3
client = boto3.client('ec2')
response = client.create_tags(
    Resources=[
        'vol-Id'
    ],
    Tags=[
        {
            'Key': 'Application',
            'Value': 'Int',
        },
        {
            'Key': 'Cost Center',
            'Value': 'Production',
        },
        {
            'Key': 'Department',
            'Value': 'Security',
        },
        {
            'Key': 'Environment',
            'Value': 'PRD',
        },
        {
            'Key': 'Name',
            'Value': 'AFRSAPVPNTEST',
        },
    ],
)

