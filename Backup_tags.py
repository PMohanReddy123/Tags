import boto3

client = boto3.client('backup')
response = client.list_tags(
    ResourceArn='arn:aws:ec2:eu-west-1::snapshot/snap-0b0eb494ab09862d7',
    # NextToken='string',
    # MaxResults=123
)

for resp in response['Tags']:
    tags=resp['Tags']
    print('The backup tags are {}'.format(tags))