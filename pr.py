import boto3

client = boto3.client('ec2')
resp = client.describe_instances()
for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        state = instance['State']['Name']
        for volume in instance['BlockDeviceMappings']:
            vol_id = volume['Ebs']['VolumeId']
            vol_status=volume['Ebs']['Status']
        print("id is {}, state is {}".format(vol_id,vol_status))

