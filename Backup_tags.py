import boto3

client = boto3.client('backup')
response = client.list_tags(
    ResourceArn='',
    # NextToken='string',
    # MaxResults=123
)

for resp in response['Tags']:
    tags=resp['Tags']
    print('The backup tags are {}'.format(tags))
