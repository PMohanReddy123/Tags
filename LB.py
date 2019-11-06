import boto3
client = boto3.client('elbv2')
response = client.add_tags(
    ResourceArns=[
        'LB_ARN'
    ],
    Tags=[
        {
            'Key': 'Name',
            'Value': 'CBSZBXAFR01',
        },
        {
            'Key': 'Application',
            'Value': 'Int',
        },
        {
            'Key': 'Cost Center',
            'Value': 'Non-Production',
        },
        {
            'Key': 'Department',
            'Value': 'Security',
        },
        {
            'Key': 'Environment',
            'Value': 'NPRD',
        },
    ]
)

