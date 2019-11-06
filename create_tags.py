import boto3
import sys

ec2 = boto3.client('ec2')
response = ec2.describe_instances(
    Filters = [
        {
            'Name': 'tag:Environment',
            'Values': ['NPRD']
        }
    ]
)
ids = []

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        state = instance['State']['Name']
        ids.append(instance['InstanceId'])
print('Instance Id = {} And Its State is {} '.format(instance_id,state))
print("Changing tags for %d instances" % len(ids))
ec2.create_tags(
    Resources=ids,
    # Tags=[
    #     {
    #         'Key': 'Cost Center',
    #         'Value': 'Non-Production'
    #     }
    # ]
    Tags=[
        {
            'Key': 'Department',
            'Value': 'Finance'
        }
    ]
)
