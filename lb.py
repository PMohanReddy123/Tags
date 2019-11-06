import boto3
client = boto3.client('elbv2')
response = client.add_tags(
    ResourceArns=[
        'arn:aws:elasticloadbalancing:eu-west-1:378457291432:loadbalancer/app/CBSSITAE02/5eea404182407f0a'
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

