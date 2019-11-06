import boto3
client = boto3.client('ec2')
response = client.create_tags(
    Resources=[
        'vol-0df2a9b5a5bc9171d'
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
# response1 = client.delete_tags(
#     Resources=[
#         'vol-045768f9c3f7edb88',
#     ],
#     Tags=[
#         {
#             'Key': 'Name1',
#             'Value': 'Mohan',
#         },
#     ],
# )
