import boto3
client = boto3.client("ec2")
response = client.describe_tags(
    Filters=[
        {
            'Name': 'Environment',
            'Values': [
                'PRD',
            ]
        },
    ],
    MaxResults=123,
    NextToken='string'
)
resp = client.describe_instances(
    Filters=[
        {
            'Name': 'tag:Environment',
            'Values': ['PRD','STG']
        }
    ]
)
for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        state = instance['State']['Name']
        # for volume in instance['BlockDeviceMappings']:
        #     vol_id = volume['Ebs']['VolumeId']
        #     vol_status=volume['Ebs']['Status']
        #     vol_attach_time=volume['Ebs']['AttachTime']
        #     print('Instance Id = {} And Its State is {} and volume id is {} and its status is {} and its attached time is {}'.format(instance_id,state,vol_id,vol_status,vol_attach_time))
        print("id is{}, state is {}".format(instance_id,state))