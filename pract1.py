import boto3

client = boto3.client('ec2')
response = client.describe_volumes()
for resp in response['Volumes']:
    for attach in resp['Attachments']:
        vol_id=attach['VolumeId']
    print('vol id is {}'.format(vol_id))