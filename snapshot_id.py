import boto3

client = boto3.client('ec2')
client1 = boto3.client('backup')

resp = client.describe_instances(
    # Filters = [
    #     {
    #         'Name': 'tag:Env',
    #         'Values': ['Prod']
    #     }
    # ]
)
response1 = client1.describe_backup_job(
    #BackupJobId='string'
    BackupJobId='CF2207C2-2760-DBF8-74D2-3E517FDC186B'
)
# print(response1)
a=[]
for response in response1['BackupJobId']:
    for b in response():
        print(a.insert(b))
    # state_list = response['State']


