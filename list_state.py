import boto3

client = boto3.client('backup')

#response = client.describe_backup_job()
response = client.describe_backup_job(
	BackupJobId='4defc715-c18a-4730-b4e6-402be2e7fb41'
)


for resp in response['BackupJobId']:
#for resp in response():
	Id=resp['BackupJobId']
	state=resp['State']
	print(f"BackupId id {Id} and its state is {state}")
